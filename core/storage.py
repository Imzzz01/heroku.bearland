from django.core.files.storage import Storage
from django.conf import settings
import cloudinary.uploader
from urllib.parse import urljoin

class CloudinaryStorage(Storage):
    """Custom storage for Cloudinary"""
    
    def _save(self, name, content):
        """Upload file to Cloudinary"""
        result = cloudinary.uploader.upload(
            content,
            public_id=f"media/{name}",
            overwrite=True,
            resource_type="auto"
        )
        return result['public_id']

    def url(self, name):
        """Generate public URL"""
        base_url = f"https://res.cloudinary.com/{settings.CLOUDINARY_CONFIG['cloud_name']}/"
        return urljoin(base_url, f"image/upload/{name}")

    def exists(self, name):
        """Check if file exists"""
        try:
            cloudinary.uploader.explicit(name, type="upload")
            return True
        except Exception:
            return False

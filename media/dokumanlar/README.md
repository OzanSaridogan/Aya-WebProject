Place PDF files here and name them with a clear title. To register a document in the site manually, create a matching database row (optional) or name files with a prefixed date for ordering.

If you prefer adding records in the DB, run the Django shell and execute:

```python
from anasayfa.models import DernekDokuman
DernekDokuman.objects.create(baslik='My Doc', aciklama='manual', dosya='dokumanlar/filename.pdf')
```

Notes:
- Files will be accessible at `/media/dokumanlar/<filename>.pdf`
- Ensure `MEDIA_URL` and `MEDIA_ROOT` are configured in `settings.py` and URLs are served correctly.

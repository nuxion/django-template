from django.contrib.staticfiles.storage import ManifestStaticFilesStorage


class NoSourceMapsStorage(ManifestStaticFilesStorage):
    """
    from https://code.djangoproject.com/ticket/33353
    """
    patterns = (
        (
            "*.css",
            (
                "(?P<matched>url\\(['\"]{0,1}\\s*(?P<url>.*?)[\"']{0,1}\\))",
                (
                    "(?P<matched>@import\\s*[\"']\\s*(?P<url>.*?)[\"'])",
                    '@import url("%(url)s")',
                ),
            ),
        ),
    )


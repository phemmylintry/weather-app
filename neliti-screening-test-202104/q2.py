class Hit(models.Model):

    PAGEVIEW = 'PV'
    DOWNLOAD = 'DL'
    ACTIONS = (
        (PAGEVIEW, 'Article web page view'),
        (DOWNLOAD, 'Article download'),
    )

    publication = models.ForeignKey('Publication', on_delete=models.CASCADE)
    date = models.DateTimeField(default=django.utils.timezone.now)
    ip_address = models.GenericIPAddressField()
    user_agent = models.ForeignKey('UserAgent', on_delete=models.SET_NULL,
                                   null=True, blank=True)
    action = models.CharField(max_length=2, choices=ACTIONS)


class Publication(models.Model):

    title = models.CharField(max_length=200)
    journal = models.ForeignKey('Journal', on_delete=models.CASCADE)
    # ... remaining fields omitted


def get_journal_statistics():
    # Construct summary dict in the form {journal_id -> (total_views, total_downloads)}
    
    journal_id = Journal.objects.all()
    get_statistics = Publication.objects.all()

    summary = {}

    for journals in journal_id.id:
        
        summary[journal] = [get_statistics.totalviews, get_statistics.total_downloads]
        

    return summary




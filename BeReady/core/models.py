from django.db import models


class User(models.Model):
    STATUS = (
        ("to do", "to do"),
        ("in process", "in process"),
        ("done", "done")
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_on = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, max_length=200, default="to do")
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)
    photo = models.ImageField(upload_to='taskList_photos',
                              validators=[validate_file_size,
                                          validate_extension],
                              null=True, blank=True)
    document = models.FileField(upload_to='taskList_documents',
                              validators=[validate_file_size, validate_extension],
                              null=True, blank=True)

    class Meta:
        verbose_name = 'TaskList'
        verbose_name_plural = 'TaskLists'

    def __str__(self):
        return '{}: {}, {}, {}, {}'.format(self.name, self.description, self.created_at, self.due_on, self.status)


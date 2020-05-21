c = get_config()

c.Exporter.template_file = 'slides_numbering'

# Configure our tag removal
c.TagRemovePreprocessor.remove_cell_tags = ("hide_cell",)
c.TagRemovePreprocessor.remove_all_outputs_tags = ('hide_output',)
c.TagRemovePreprocessor.remove_input_tags = ('hide_input',)

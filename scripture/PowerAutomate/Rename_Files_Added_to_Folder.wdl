## Remove 'T' from file PDF file name

if(
   contains(triggerBody()?['{FilenameWithExtension}'], 'T'),
   concat(
      substring(triggerBody()?['{FilenameWithExtension}'], 0, indexOf(triggerBody()?['{FilenameWithExtension}'], 'T')),
      '.pdf'
   ),
   triggerBody()?['{FilenameWithExtension}']
)


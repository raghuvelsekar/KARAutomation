 $Outlook = New-Object -ComObject Outlook.Application
 $createmail = $Outlook.CreateItem(0)
 $createmail.To =  "raghuvel.sekar@karglobal.com"
 $createmail.Subject = "test"
 $createmail.Body = "less then 100 exit"
 $createmail.Send()
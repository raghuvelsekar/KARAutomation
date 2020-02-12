 $Outlook = New-Object -ComObject Outlook.Application
 $createmail = $Outlook.CreateItem(0)
 $createmail.To =  "raghuvel.sekar@karglobal.com"
 $createmail.Subject = "test"
 $createmail.Body = "test"
 $file = "C:\Users\raghuvel.sekar\Desktop\KARscreenshot3.jpg"
 $file1 = "C:\Users\raghuvel.sekar\Desktop\KARscreenshot4.jpg"
 $createmail.Attachments.Add($file)
 $createmail.Attachments.Add($file1)
 $createmail.Send()
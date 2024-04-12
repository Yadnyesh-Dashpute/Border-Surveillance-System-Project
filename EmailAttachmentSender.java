import java.io.IOException;
import java.util.Date;
import java.util.Properties;

import javax.mail.Authenticator;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Multipart;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.AddressException;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeBodyPart;
import javax.mail.internet.MimeMessage;
import javax.mail.internet.MimeMultipart;
import javax.swing.JOptionPane;

public class EmailAttachmentSender
{
public static void main(String args[])
{
	
	//mailsentwithphoto(email,loc);
	mailsentwithphoto("bordersurveillance@yahoo.com", "C:\\project\\snap.png");
}
	
	
	public static void sendEmailWithAttachments(String host, String port,final String userName,
			                                    final String password, String toAddress,String subject,
			                                    String message, String[] attachFiles)throws AddressException, MessagingException
    {

		Properties properties = new Properties();
		properties.put("mail.smtp.host", host);
		properties.put("mail.smtp.port", port);
		properties.put("mail.smtp.auth", "true");
		properties.put("mail.smtp.starttls.enable", "true");
		properties.put("mail.user", userName);
		properties.put("mail.password", password);
		properties.put("mail.smtp.ssl.trust", "smtp.gmail.com");


		Authenticator auth = new Authenticator()
		{
			public PasswordAuthentication getPasswordAuthentication()
			{
				return new PasswordAuthentication(userName, password);
			}
		};

		Session session = Session.getInstance(properties, auth);

		Message msg = new MimeMessage(session);

		msg.setFrom(new InternetAddress(userName));

		InternetAddress[] toAddresses = { new InternetAddress(toAddress) };

		msg.setRecipients(Message.RecipientType.TO, toAddresses);
		msg.setSubject(subject);
		msg.setSentDate(new Date());

		MimeBodyPart messageBodyPart = new MimeBodyPart();

		messageBodyPart.setContent(message, "text/html");

		Multipart multipart = new MimeMultipart();

		multipart.addBodyPart(messageBodyPart);

		if (attachFiles != null && attachFiles.length > 0)
		{
			for (String filePath : attachFiles)
			{
				MimeBodyPart attachPart = new MimeBodyPart();

				try
				{
					attachPart.attachFile(filePath);
				}
				catch (IOException ex)
				{
					ex.printStackTrace();
				}

				multipart.addBodyPart(attachPart);
			}
		}

		msg.setContent(multipart);

		Transport.send(msg);
	}

	//public static void main(String args[])
	public static void mailsentwithphoto(String flatEmail,String visitorphotopath)
	{
		String host = "smtp.gmail.com";
		String port = "587";
		//String mailFrom = "projectotpdetail@gmail.com";
		String mailFrom = "diplomaproject05@gmail.com";
		//String password = "isxynjzzywpbscyd";
		String password = "mlfkzhevorhdcjru";
		  

		 String mailTo = flatEmail;
		 System.out.println("Flat Onwer EMail="+mailTo);
		//String mailTo = "amolpatil37@yahoo.com";
		String subject = "Email For Visitor Verification with Photo attachments";
		String message = "Alert! Intruder Has Been Detected";

		String[] attachFiles = new String[1];
		//attachFiles[0] = "C:\\Users\\DMG\\Documents\\Face_Temperture_Project\\VisitorData\\7867564534.jpg";   //visitorphotopath;
		attachFiles[0] = visitorphotopath;
		System.out.println("Photo sent to Onwer EMail="+attachFiles[0]);

		try
		{
			sendEmailWithAttachments(host, port, mailFrom, password, mailTo,subject, message, attachFiles);
			System.out.println("Email sent.");
			JOptionPane.showMessageDialog(null,"Email With Photo Send to Flat Owner Successfully !!!");
		}
		catch (AddressException ex)
		{
			System.out.println("Could not send email.");
			ex.printStackTrace();

		}
		catch (MessagingException e)
		{
			System.out.println("not send email.");
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
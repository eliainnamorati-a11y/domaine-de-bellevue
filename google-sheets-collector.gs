/**
 * Domaine de Bellevue - Automated Form Submissions Collector
 * 
 * HOW TO SETUP (Takes 60 seconds):
 * 1. Open https://sheets.new to create a new Google Sheet.
 * 2. Name the sheet: "Domaine de Bellevue - Inquiries"
 * 3. In the top menu, click Extensions > Apps Script.
 * 4. Paste all of this code into the editor, replacing any existing code.
 * 5. Click "Save" (floppy disk icon).
 * 6. Click "Deploy" (top right) > "New deployment".
 * 7. In "Select type" (gear icon), select "Web app".
 * 8. Set:
 *    - Description: "Domaine de Bellevue Form Collector"
 *    - Execute as: "Me" (your Google account)
 *    - Who has access: "Anyone"
 * 9. Click "Deploy", approve permissions (Advanced > Go to script).
 * 10. Copy the "Web app URL" (starts with https://script.google.com/macros/s/...)
 * 11. Send that URL here or paste it into index.html!
 */

function doPost(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    // Set headers if the sheet is empty
    if (sheet.getLastRow() === 0) {
      sheet.appendRow([
        "Date (CET)",
        "Prénom",
        "Nom",
        "Email",
        "Téléphone",
        "Message",
        "Langue",
        "URL"
      ]);
      sheet.getRange(1, 1, 1, 8).setFontWeight("bold").setBackground("#f3efe6");
      sheet.setFrozenRows(1);
    }

    var data = {};
    if (e.postData && e.postData.contents) {
      try {
        data = JSON.parse(e.postData.contents);
      } catch (jsonErr) {
        data = e.parameter || {};
      }
    } else if (e.parameter) {
      data = e.parameter;
    }

    var now = new Date();
    var timestamp = Utilities.formatDate(now, "Europe/Zurich", "yyyy-MM-dd HH:mm:ss");
    var firstname = data.firstname || data["Prénom"] || "";
    var lastname = data.lastname || data["Nom"] || "";
    var email = data.email || data["Email"] || "";
    var phone = data.phone || data["Téléphone"] || "";
    var message = data.message || data["Message"] || "";
    var lang = data.lang || "FR";
    var pageUrl = data.url || "https://www.domaine-de-bellevue.ch/";

    // Append to Google Sheet permanently
    sheet.appendRow([
      timestamp,
      firstname,
      lastname,
      email,
      phone,
      message,
      lang,
      pageUrl
    ]);

    // Send instant email notification directly to elia.innamorati@gmail.com and elia@innamorati.ch
    var emailSubject = "Nouvelle demande Domaine de Bellevue: " + firstname + " " + lastname;
    var emailBody = 
      "Nouvelle demande reçue sur Domaine de Bellevue:\n\n" +
      "Date: " + timestamp + "\n" +
      "Nom: " + firstname + " " + lastname + "\n" +
      "Email: " + email + "\n" +
      "Téléphone: " + phone + "\n" +
      "Message:\n" + message + "\n\n" +
      "Page: " + pageUrl;

    MailApp.sendEmail({
      to: "elia.innamorati@gmail.com",
      cc: "elia@innamorati.ch",
      subject: emailSubject,
      body: emailBody
    });

    return ContentService
      .createTextOutput(JSON.stringify({ status: "success", collected: true }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: "error", message: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  return ContentService.createTextOutput("Domaine de Bellevue Form Collector Active.");
}

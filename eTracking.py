// Design the tracking system, allowing the user to use an User ID to search for status associated with that ID.

// Tracking System consists of three Google sheets:
// User interface, where the search box and result box exist.

Set SearchBox = C5
Set Result = C7

// First, get the position of the User ID in column A (User ID database) that matches the User ID typed in C5.

=MATCH(C5, dataBase!A:A, 0)

// Then, get the status data in column B of that User ID, where C5 matches the user ID in the database, exactly (0 code).
=INDEX(dataBase!B:B, MATCH(C5, dataBase!A:A, 0)

// If N/A, then shows รหัสไม่ถูกต้อง โปรดลองอีกครั้ง ติดต่อเจ้าหน้าที่ โทร. 0 2265 6223-5 ค่ะ, else show the status data. 

// Hence, we have:
Set C7=IFNA(INDEX(dataBase!B:B, MATCH(C5, dataBase!A:A, 0)),"รหัสไม่ถูกต้อง โปรดลองอีกครั้ง ติดต่อเจ้าหน้าที่ โทร. 0 2265 6223-5 ค่ะ")

// Hide this fomula by referring to the cell in the background engine in another sheet that will be hided, called 'trackAI', which is simply the copy of the UI sheet.

// The search box in trackAI will get the search data from the UI sheet (eTracking) search box (C4)
Set C4=eTracking!C4

// Set the real status box, which shows result in the background sheet
Set =C7=IFNA(INDEX(dataBase!B:B, MATCH(C5, dataBase!A:A, 0)),"รหัสไม่ถูกต้อง โปรดลองอีกครั้ง ติดต่อเจ้าหน้าที่ โทร. 0 2265 6223-5 ค่ะ" 

// Go back to eTrack sheet, the status box gets the data from the status box in the background sheet. 
C7=trackAI!C7

// Hide the trackAI sheet. So, the user will only see the simplified fomula: trackAI!C7 instead.

// Protect every cell except the search box.

// Build the dataBase sheet, with two key columns: User ID (dataBase!A:A) and Status (dataBase!B:B).

// Embed the sheet in your page at Google Site, and publish it. 


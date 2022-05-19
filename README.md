## Algorithm
Tracking system allows the user to key his or her User ID to search for infomation associated with that ID. Tracking System consists of three Google sheets in one workbook.

__1. User interface__

where the search box and the output box exist.
```
Set SearchBox = C5
Set Output= C7
```

First, get the position of the User ID in column A (User ID database) that matches the User ID typed in C5.
```
=MATCH(C5, dataBase!A:A, 0)
```
Then, get the status data in column B of that User ID, where C5 matches the user ID in the database, exactly (0 code).
```
=INDEX(dataBase!B:B, MATCH(C5, dataBase!A:A, 0)
```
If N/A, then shows รหัสไม่ถูกต้อง โปรดลองอีกครั้ง ติดต่อเจ้าหน้าที่ โทร. 0 2265 6223-5 ค่ะ, else show the status data. Hence, we have:
```
Set C7=IFNA(INDEX(dataBase!B:B, MATCH(C5, dataBase!A:A, 0)),"รหัสไม่ถูกต้อง โปรดลองอีกครั้ง ติดต่อเจ้าหน้าที่ โทร. 0 2265 6223-5 ค่ะ")
```
__2. trackAI__

Hide this fomula by referring to the cell in the background engine in another sheet that will be hided, called 'trackAI', which is simply the copy of the UI sheet.
The search box in trackAI will get the search data from the UI sheet (eTracking) search box (C4)
```
Set C4=eTracking!C4
```
Set the real status box, which shows result in the background sheet
```
Set =C7=IFNA(INDEX(dataBase!B:B, MATCH(C5, dataBase!A:A, 0)),"รหัสไม่ถูกต้อง โปรดลองอีกครั้ง ติดต่อเจ้าหน้าที่ โทร. 0 2265 6223-5 ค่ะ" 
```
Go back to eTrack sheet, the status box gets the data from the status box in the background sheet. 
```
C7=trackAI!C7
```
Hide the trackAI sheet. So, the user will only see the simplified fomula: trackAI!C7 instead.

Protect every cell except the search box.

__3. dataBase__

Build the dataBase sheet, with two key columns: User ID (dataBase!A:A) and Status (dataBase!B:B).

Embed the sheet in your page at Google Site, and publish it. 

__4. Official UI__

Add more columns to the database sheet (dataBase), with the following headers in Row 1:
```
A B C D E F G
ID Status Title Name Email Phone Date
```
Create a new sheet, named "Update", which is a form for keying new information to update the datatbase.

Locked all cells except the input cells: 

```
Search: B3
ID: B6 
Name: B10
Email: D6
Phone: D8
Date: D10
Status: B12 
```
Insert three command buttons: Search, Save, and Clear.

Add Apps Scripts:

```
function ClearAllCells() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var formS = ss.getSheetByName("Update");
  var rangesToClear = ["B3", "B6", "B8", "B10", "D6", "D8", "D10", "D12"];
  for (var i=0; i<rangesToClear.length; i++){ 
  formS.getRange(rangesToClear[i]).clearContent();
  }
};

function SubmitData() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var update = ss.getSheetByName("Update");
  var dataS = ss.getSheetByName("dataBase");
  var values = [[update.getRange('B6').getValue(),
                update.getRange('D12').getValue(),
                update.getRange('B8').getValue(),
                update.getRange('B10').getValue(),
                update.getRange('D6').getValue(),
                update.getRange('D8').getValue(),
                update.getRange('D10').getValue()]];
dataS.getRange(dataS.getLastRow()+1, 1, 1, 7).setValues(values);
ClearAllCells();
}

var SEARCH_COL_IDX = 0;
function Search() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var formS = ss.getSheetByName("Update"); //Form Sheet
  var str = formS.getRange("B3").getValue();
  var values = ss.getSheetByName("dataBase").getDataRange().getValues();
  for (var i = 0; i < values.length; i++) {
    var row = values[i];
    if (row[SEARCH_COL_IDX] == str) {
      formS.getRange("B6").setValue(row[0]) ;
      formS.getRange("D12").setValue(row[1])
      formS.getRange("B8").setValue(row[2]) ;
      formS.getRange("B10").setValue(row[3]);
      formS.getRange("D6").setValue(row[4]) ;
      formS.getRange("D8").setValue(row[5]) ;
      formS.getRange("D10").setValue(row[6]) ;
    }}}
```



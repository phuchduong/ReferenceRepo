// Load the text file into memory
val dwellText = sc.textFile(
	"wasb://brucewaynespark@dojodemo.blob.core.windows.net/hive/warehouse/hivesampletable/HiveSampleData.txt"
)

// Create an empty object, define schema
case class webDwell(
	clientid: String,
	querytime: String,
	market: String,
	deviceplatform: String,
	devicemake: String,
	devicemodel: String,
	state: String,
	country: String,
	querydwelltime: String,
	sessionid: Integer,
	sessionpagevieworder: Integer
)

// Map the text file, separated by tabs, to the object, as a data frame.
val dwellTb = dwellText.map(s => s.split("\t")).map(
	s => webDwell(
			s(0),
			s(1),
			s(2),
			s(3),
			s(4),
			s(5),
			s(6),
			s(7),
			s(8),
			s(9).toInt,
			s(10).toInt
    )
).toDF()

// turns the dwell object into a dwell table in scala
dwellTb.registerTempTable("dwellTable")

%sql
select * from dwellTable
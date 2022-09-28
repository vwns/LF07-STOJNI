int TR_PIN = A0;
double a1, b1, c1, d1, r2, r1, vo, tempC, tempF, tempK;

void setup()
{
  Serial.begin(9600);
  a1 = 3.354016E-03 ;
  b1 = 2.569850E-04 ;
  c1 = 2.620131E-06 ;
  d1 = 6.383091E-08 ;

  r1 = 9720.0;

  pinMode(TR_PIN, INPUT);

}

void loop()
{

  // read the temp
  vo = analogRead(TR_PIN);
  vo = vo / (1023.0 / 5.0);

  // voltage divider calculation
  // vo = 5 * r2 /(r1+r2)
  // solve for r2
  // get the exact value for voltage divider r1

  r2 = ( vo * r1) / (5.0 - vo);

  //equation from data sheet
  tempK = 1.0 / (a1 + (b1 * (log(r2 / 10000.0))) + (c1 * pow(log(r2 / 10000.0), 2.0)) + (d1 * pow(log(r2 / 10000.0), 3.0)));
  tempC  = ((tempK - 273.15) * -1);
  tempF  = (tempC * 1.8) + 32.0;


  Serial.println(String(tempC));
  delay(1000);
  
}

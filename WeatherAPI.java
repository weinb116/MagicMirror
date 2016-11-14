import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

/**
 * Created by Aaron on 11/13/2016.
 */
public class WeatherAPI {
    public static void main(String[] args) throws IOException {

      httpGet("http://api.openweathermap.org/data/2.5/weather?zip=92868,us&APPID=caf4e76ba40944f2e450506e7ff793da");


        // JSONObject json = readJsonFromUrl("http://api.openweathermap.org/data/2.5/forecast/city?id=524901&APPID={caf4e76ba40944f2e450506e7ff793da}");
        // System.out.println(json.toString());
        // System.out.println(json.get("weather.id"));


    }
    public static String httpGet(String urlStr) throws IOException {
        URL url = new URL(urlStr);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        // if (conn.getResponseCode() != 200) {
        //     throw new IOException(conn.getResponseMessage());

        // }
        BufferedReader rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = rd.readLine()) != null) {
            sb.append(line);

        }
        rd.close();
        conn.disconnect();
        // System.out.println(sb.toString());

        parseData(sb.toString());
        return (sb.toString());
    }
    public static String parseData(String data){
      String[] myData = data.split(",");
      for(int i = 0; i<myData.length -1; i++)
      {
        System.out.println(myData[i]);
      }
      return ("done");
    }

}

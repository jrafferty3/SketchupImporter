using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.IO;
using System.Collections;
using HtmlAgilityPack;
using System.Diagnostics;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            string file = "C:/Users/Patrick/Documents/models.txt";
            try
            {
                StreamReader reader = File.OpenText(file);
                string line;
                while ((line = reader.ReadLine()) != null)
                {
                   aSyncSearchForModel(line.Substring(0,line.IndexOf(" ")),line.Substring(line.IndexOf(" ")+1));
                }
            }
            catch(Exception e)
            {
                //oops
            }
        }

        private static IEnumerator aSyncSearchForModel(string filename, string searchterm)
        {
            WebClient w = new WebClient();
            string htmlstring = w.DownloadString("http://sketchup.google.com/3dwarehouse/doadvsearch?title=" + searchterm.Replace(" ","+")
                                        + "&scoring=d&btnG=Search+3D+Warehouse&dscr=&tags=&styp=m&complexity=any_value&file="
                                        + "zip" + "&stars=any_value&nickname=&createtime=any_value&modtime=any_value&isgeo=any_value&addr=&clid=");
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.LoadHtml(htmlstring);

            
            //Grab a result from the search page
            HtmlAgilityPack.HtmlNodeCollection results = doc.DocumentNode.SelectNodes("//div[@class='searchresult']");
            string model_page_url = "http://sketchup.google.com" + results[0].SelectSingleNode(".//a").Attributes["href"].Value;
            htmlstring = w.DownloadString(model_page_url);
            doc.LoadHtml(htmlstring);

            //Find the downloadable zip file
            results = doc.DocumentNode.SelectNodes("//a[contains(@href,'rtyp=zip')]");
            foreach (HtmlNode r in results)
            {
                HtmlAttribute src = r.Attributes["href"];
                string url = "http://sketchup.google.com" + src.Value;
                url = url.Replace("&amp;", "&");
                string location = @"C:\Users\Patrick\Downloads\" + filename + ".zip";
                System.Diagnostics.Debug.WriteLine(url+"\n"+location);
                w.DownloadFile(new Uri(url),location);
            }
            return null;
        }

    }
}

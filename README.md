This is a Python script that compiles csv files of blog post views from Wordpress' Jetpack.<br>
The wordpress website is under a Business Plan, equipped with Jetpack plug-in.<br>
<br>
![image](https://github.com/user-attachments/assets/218e548f-60c9-4045-a6e1-f9ff6caf99ba) <br>
<br>
As there is currently no other way to download data except as to save them as csv files <a href = "https://wordpress.org/support/topic/site-not-commercial-give-us-an-option-to-export-stats/" target="_blank">(link)</a>, I made a Python script that puts together data from all the downloaded csv files.<br>
<br>
<h3>How it works:</h3>
<ol>
  <li>Make sure all csv files are saved in a target folder.</li><br>
  <img width="250" alt="image" src="https://github.com/user-attachments/assets/288d0828-dcc7-4329-9b6a-1fa678b45382"><br>
  <br>
  <li>The Jetpack stats have no headers, has 3 columns corresponding to the post title, views and the URL.</li><br>
  <img width="1389" alt="image" src="https://github.com/user-attachments/assets/9dc0cac6-0b2b-4385-8981-e854626b7b1e"><br>
  <br>
  <li>The program creates a dataframe that will contain the relevant data.</li><br>
  <br>
  <li>For every csv file, the program takes the month label from the filename and creates a new column that will contain the views of each post. The resulting dataframe will have the following columns: Post title (values: titles) and 1 month for every available file (values: views).</li><br>
  <br>
  <li>The program outputs a csv file in a nested folder labeled "results". This is an example of the table that combines all the monthly views.</li><br>
  <img width="1385" alt="image" src="https://github.com/user-attachments/assets/762a24ac-8cc5-4f4e-98d8-33c22398105d"><br>
  <br>
  <li>Additionally, if you are doing data analysis on the site analytics, the program also outputs the data into <em>long format</em> via <strong>pd.melt</strong> for easier data visualization with your tool of choice. It outputs a csv file labeled "tidy" in the results folder.</li><br>
  <img width="448" alt="image" src="https://github.com/user-attachments/assets/ac7b659a-9eab-40cc-b88e-9293c8cfb041"><br>
  <br>
  You can study your analytics easier:<br><br>
  <img width="852" alt="image" src="https://github.com/user-attachments/assets/0f24891a-085b-4c24-96b8-5db43e7a7daa">
</ol>
<br>




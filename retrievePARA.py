from bs4 import BeautifulSoup
html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>An example of HTML page</title>
</head>
<body>
<h2>This is an example HTML page</h2>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
euismod porta.</p>
<p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from
w3resource.com</a></p>
<p><a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from 
w3resource.com</a></p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print("Here you go, sir:")
print(soup.find_all("p"))
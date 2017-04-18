import webapp2 

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('Nombre: Pablo Silva Bravo')


class dolaresAPesos(webapp2.RequestHandler):
    def get(self,dolares):
        pesos = int(dolares)*663
    	self.response.write('Conversion de dolares a pesos')
    	self.response.out.write('''
            <html>
                <body>
                	<table>
                		<tr>
                			<td>
                				<img src ='../../fotos/dolar.jpg' width='400px'/>
                				<p> %s USD</p>
                			</td>
                			<td>
                				<img src ='../../fotos/peso.jpg' width='400px' />
                				<p> %s CLP</p>
                			</td>
                		</tr>
                	</table>                
                 </body>
            </html>
        ''' %(dolares,pesos))

class pesosADolares(webapp2.RequestHandler):
    def get(self,pesos):
        dolares = float(pesos)/663  

        self.response.write('Conversion de pesos a dolares')
        self.response.out.write('''
            <html>
                <body>
                    <table>
                        <tr>
                            <td>
                                <img src ='../../fotos/peso.jpg' width='400px' />
                                <p> %s CLP</p>
                            </td>
                            <td>
                                <img src ='../../fotos/dolar.jpg' width='400px'/>
                                <p> %s USD</p>
                            </td>
                        </tr>
                    </table>                
                 </body>
            </html>
        ''' %(pesos,dolares))

app = webapp2.WSGIApplication([
    ('/',MainPage),
    ('/(\d+)/usd/clp',dolaresAPesos), 
    ('/(\d+)/clp/usd',pesosADolares),       
], debug=True)



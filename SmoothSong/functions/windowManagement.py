import webbrowser


class WindowManagementClass:
    # OPEN PAYPAL PAGE IN BROWSER
    @staticmethod
    def openPayPal():
        url = "https://www.paypal.com/ro/business"
        webbrowser.open(url, new=1)

    # CLOSE THE APP
    @staticmethod
    def exitApp(window):
        window.destroy()

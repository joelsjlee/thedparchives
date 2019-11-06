from bs4 import BeautifulSoup
import requests
import sys



def initialize():
    #open xml with Beautiful Soup
    with open("dparchives.library.upenn.edu.xml") as dplist:
        soup = BeautifulSoup(dplist, "xml")
    #Create a list of all the documents Ids
    documentIDList = soup.find_all('DocumentID')
    return documentIDList

def getPageText(issue_ID, directory) :
    #Grab url of issue
    url_template = 'https://dparchives.library.upenn.edu/?a=d&d={}&f=XML'
    url = url_template.format(issue_ID.get_text())
    #Grab XML of the single issue
    r = requests.get(url)
    issue_soup = BeautifulSoup(r.content, "xml")
    #Create list of Page IDs from XML
    document_page_list = issue_soup.find_all('PageID')
    #For loop to run over every page in PageID list
    issue_txt = ''
    for pageID in document_page_list :
        #Grab url of page
        page_url = url_template.format(pageID.get_text())
        #Grab XML of single page
        page_request = requests.get(page_url)
        page_soup = BeautifulSoup(page_request.content, "xml")
        #Grab text of a single page from XML
        text = page_soup.find("PageTextHTML").get_text()
        clean_txt = BeautifulSoup(text, "lxml").text
        issue_txt = issue_txt + ' ' + clean_txt
    #Make a name for the text file
    file_name_template = directory
    file_name = file_name_template.format(issue_ID.get_text())
    #Write and save the file
    with open(file_name, 'w', encoding="utf-8") as f:
        f.write(issue_txt)

def run(documentIDList, start = 1):
    for i, doc_ID in enumerate(documentIDList[start:], start=start):
        print(i, flush=True)
        start += 1
        getPageText(doc_ID, 'C:/Users/Joel/thedparchives/dpIssueTexts/{}.TXT')


if __name__ == '__main__':
    if (len(sys.argv) < 2) :
        run(initialize())
    else:
        start = int(sys.argv[1])
        run(initialize(), start)

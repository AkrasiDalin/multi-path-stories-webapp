#! /usr/bin/ python
#!flask/bin/python


from flask import Flask, session, redirect, url_for, escape, request, render_template
app = Flask(__name__)
app.secret_key = 'qwerty'

# pages object with default page pre-existent
# pages can contain multiple page(s), each of which contains from one
# to multiple sentences to which 3 main datas are attached
pages = {1:{1:{'sentence':'once upon a time','isclicked':'false','page':1}}}

# used for new pages mainly ad shortcut
page_counter = len(pages)+1

# keeps track of current page in use
current_page = 1

# generates new page ad updates global variables
def createPage(_content):
    global page_counter
    page_counter = len(pages)+1

    global current_page
    current_page = len(pages)

    addPage('page'+str(page_counter), _content)
    page_counter = len(pages)+1
    current_page = len(pages)


# servo tool used by createPage
# it generates a new sentence object and adds it to the new page
def addPage(_page, _content):
    _page = {1:{'sentence': _content,'isclicked':'false','page':page_counter}}
    if len(pages) <= 0:
        pages[page_counter] = _page
    else:
        for i in range(1,len(pages)+1):
            if not pages[i] == _page:
                pages[page_counter] = _page



# add content to given page at given coordinates
def addContent(page_index, index, sentence):
    pages[page_index][index] = {'sentence':sentence,'isclicked':'false','page':current_page}

# modifies content of a given page to given coordingates
def modifyPhraseData(page_index, index, sentence,isclicked, newpage):
    pages[page_index][index] = {'sentence':sentence, 'isclicked':isclicked,'page':newpage}

# routes to main page (table) with up to date pages content and current page in request
@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html',stories=pages[current_page], page_index=current_page)



# will take sentence and page counter number
# if page counter exists then it will redirect to that page
# else it will create a new one for it
@app.route('/linkPage/<pageindex>/<index>/<sentence>/<isclicked>', methods=['GET','POST'])
def linkPage(pageindex,index,sentence,isclicked):

    if isclicked == 'true':
        return redirect('/redirectToPage/'+pageindex)
    else:
        modifyPhraseData(current_page, int(index), sentence, 'true', page_counter)
        return redirect('/newPage/'+sentence)


# will take sentence and create a new page with 1st entry = sentence
# then it will show a page with that content in
@app.route('/newPage/<sentence>', methods=['GET','POST'])
def newPage(sentence):
    global current_page
    current_page = len(pages)
    createPage(sentence)
    page_content = pages[current_page]

    return redirect(url_for('index'))



# it will take a page index and populate html with its content
@app.route('/redirectToPage/<page>', methods=['GET','POST'])
def redirectToPage(page):
    global current_page
    current_page = int(page)

    page_content = pages[current_page]
    return redirect(url_for('index'))


# takes index of given story sentence and adds it to the story page
@app.route('/attachToView/<index>', methods=['GET','POST'])
def attachToView(index):
    if len(request.form['sentence']) >= 1:
        addContent(current_page, int(index), request.form['sentence'])
        page_content = pages[current_page]

    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)

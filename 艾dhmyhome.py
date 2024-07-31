#记得改文件名
'''我的主页'''
import base64
import time
import streamlit as st
from PIL import Image,ImageOps,ImageFilter
page=st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区','我的个人主页','热梗知识考察'])

def bar_bg(img):
    last = 'png'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

def page_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )
    
bar_bg('绿色.png')
page_bg('背景.jpg')

def image_change(img,rc,gc,bc):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img

def red(img):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][0]
            g=img_array[x,y][1]
            b=img_array[x,y][2]
            if r <=100:
                r+=150
            elif r<=150 and r>100:
                r+=100
            else:
                r+=50
            img_array[x,y]=(r,g,b)
    return img

def gray(img):
    width,height=img.size
    img_gray=img.convert('L')
    return img_gray

def page_1():
    '''我的兴趣推荐↓'''
    st.write(":green[我是练习时长两年半的个人练习生艾定航]:smile:")
    col1,col2=st.columns([1,1])
    with col1:
        st.link_button('关注我','https://space.bilibili.com/1109104601?spm_id_from=333.1007.0.0')
    with col2:
        if st.button('点赞'):
            st.write(':感谢支持')
    st.write("我对网络热梗比较感兴趣，我可以为你们推荐几个我认为比较好的梗")
    st.write("No.1:鸡你太美")
    st.image("艾dh坤哥.jpg")
    st.write(":red[↓点击下面聆听鸡哥唱歌]")
    with open("艾dh只因你太美.mp3", "rb") as f:
        mymp3 = f.read()
    st.audio(mymp3, format="audio/mp3", start_time=0)
    st.write("No.2:华强买瓜")
    st.image("艾dh华强买瓜2.gif")
    st.write(":red[↓点击下面聆听华强版《萨日朗》]")
    with open("艾dh萨日朗.mp3", "rb") as f:
        mymp3_2 = f.read()
    st.audio(mymp3_2, format="audio/mp3", start_time=5)
    st.write("No.3:听声辨位")
    st.image('艾dh听不清楚.jpg')
    st.write(':red[↓点击下面聆听听声辨位原声素材]')
    with open('艾dh听声辩位.mp3','rb')as f:
        mymp3_3=f.read()
    st.audio(mymp3_3,format='audio/mp3',start_time=6)

def page_2():
    '''我的图片处理工具↓'''
    st.write("图片处理工具:sunglasses:")
    uploaded_file=st.file_uploader("上传图片",type=['jpg','png','jpeg'])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(['原图','改色1','改色2','改色3','变灰','一键红温'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(image_change(img,2,1,0))
        with tab3:
            st.image(image_change(img,0,2,1))
        with tab4:
            st.image(image_change(img,1,0,2))
        with tab5:
            st.image(gray(img))
        with tab6:
            st.image(red(img))
        file_name = 'new' + file_name
        img.save(file_name)
        with open(file_name,'rb')as file:
            btn=st.download_button(
                label='下载此图',
                data=file,
                file_name=f"{file_name}_改图.png",
                mime='image/png'
            )
    

def page_3():
    '''我的智慧词典↓'''
    st.write("智慧词典:sunglasses:")
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]

    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list=f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split('#')
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
        
    word=st.text_input('输入要查询的单词：')
    if word in words_dict:
        roading = st.progress(0, '开始加载')
        for i in range(1, 101, 1):
            time.sleep(0.02)
            roading.progress(i, '正在查询'+str(i)+'%')
        roading.progress(100, '查询完毕！')
        time.sleep(1.00)
        roading.empty()
        st.write('该词的意义是：',words_dict[word][1])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message=''
            for k,v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
                message = message[:-1]
                f.write(message)
            
            st.text(word+'的查询次数为：'+str(times_dict[n]))
            if word == 'hello':
                st.code('''你发现了彩蛋，你过关！''')
                st.balloons()
                st.snow()   
    elif word == '':
        pass    
    else:
        roading = st.progress(0, '开始加载')
        for i in range(1, 101, 1):
            time.sleep(0.01)
            roading.progress(i, '正在查询'+str(i)+'%')
        roading.progress(100, '查询完毕！')
        time.sleep(1.00)
        roading.empty()
        st.write('查无此词')

def page_4():
    '''我的留言区↓'''
    st.write('我的留言区:sunglasses:')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list=f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '郝哥':
            with st.chat_message('🍉'):
                st.write(i[1],':',i[2])
        elif i[1] == '刘华强':
            with st.chat_message('🔪'):
                st.write(i[1],':',i[2])
        elif i[1] == '游客':
            with st.chat_message('💩'):
                st.text(i[1]+':'+i[2])
        elif i[1]!='游客' and i[1]!='郝哥' and i[1]!='刘华强':
            with st.chat_message('❔'):
                st.text(i[1]+':'+i[2])
                
    name = st.selectbox('我是……', ['刘华强', '郝哥','游客','其他'])
    if name == '其他':
        name=st.text_input('请输入你的名字')
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
            
def page_5():
    '''我的个人主页↓'''
    st.write('我的个人主页:sunglasses:')
    picture=[]
    for i in ['主页.png','主页2.png']:
        img=Image.open(i)
        img=img.resize((300,200))
        picture.append(img)
    col1,col2=st.columns([1,1])
    with col1:
        st.write('我的b站号')
        st.image(picture[0])
    with col2:
        st.write('我的头条号')
        st.image(picture[1])
    link=st.selectbox('进入...',['头条','B站'])
    if link == '头条':
        st.link_button('点击进入'+link,'https://www.toutiao.com/c/user/token/MS4wLjABAAAAv5h9Ue3ZQLxNnCq26Hr3-gGB-GhthuaKQH1ivCdzycSuuEKFd2uLdIce4beQS3pz/?')
    elif link == 'B站':
        st.link_button('点击进入'+link,'https://space.bilibili.com/1109104601?spm_id_from=333.1007.0.0')

def page_6():
    '''热梗知识考察'''
    st.write('本关考验你，梗知识功夫:sunglasses:')
    answer=['A.秤下面有吸铁石','A.西南方','B.王大队长','C.两个都穿过','B.鲁H']
    choice1 = st.radio(
    '第一题:华强买瓜中，郝哥的秤有什么问题？',
    ['A.秤下面有吸铁石', 'B.秤被异形吃了', 'C.秤是金子做的']
)
    choice2 = st.radio(
    '第二题:听声辩位中，光头弟子第一次选了哪个方向？',
    ['A.西南方', 'B.东南方', 'C.东北方']
)
    choice3 = st.radio(
    '第三题:鸡汤来咯中，谁让穿山甲炖的鸡汤？',
    ['A.薛司令', 'B.王大队长', 'C.杜孝先']
)
    choice4 = st.radio(
    '第四题:牢大穿的是几号球衣？',
    ['A.24号', 'B.8号', 'C.两个都穿过']
)
    choice5 = st.radio(
    '第五题:全网呼叫山东人中，济宁的车牌是鲁什么？',
    ['A.鲁G', 'B.鲁H', 'C.鲁J']
)
    choice=[choice1,choice2,choice3,choice4,choice5]
    col1,col2=st.columns([1,2])
    with col1:
        if st.button('计算成绩'):
            score=0
            for i in choice:
                if i in answer:
                    score += 20                
            if score >= 100:
                st.write('你的成绩高达：'+str(score)+'，你就是一代梗王！')
            elif score >= 60 and score <80:
                st.write('你的成绩为：'+str(score)+'，你对网络热梗比较了解。')
            else:
                st.write('你的成绩只有：'+str(score)+'，你不太懂网络热梗')
    with col2:
        st.text('满分一百分，你能达到多少？试试吧。')
    

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '我的个人主页':
    page_5()
elif page == '热梗知识考察':
    page_6()


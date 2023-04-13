import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

def set_page() : 
    return st.set_page_config(page_title="DL", page_icon=":smiley:", layout="wide")

def set_background():
    return st.markdown("""<style>
                        .main {
                            background-image: url('https://i.imgur.com/PSeW0pm.gif');
                            background-size: cover;
                        }
                        </style> """, unsafe_allow_html=True)


def start_background() : 
    return st.markdown("""<style>
                        .main {
                            background-image: url('https://i.imgur.com/idnsDBs.gif');
                            background-size: cover;
                        }
                        </style> """, unsafe_allow_html=True)

def title_ment(area, direction) : 
    return st.markdown(f"<div style='background-color: green; \
                        padding: 10px; color: white; font-size: 48px;\
                        font-weight: bold; display: inline-block;'> \
                        👉{area} {direction} \
                        </div>", unsafe_allow_html=True)

def cutting() : 
    return st.markdown("---")

def result_chart() : 
    return st.image("https://i.imgur.com/NuieMp3.png", width = 1200)

# def total_load():
#     total = pd.read_csv("DL_Project/Data_csv/total.csv", encoding="utf-8")

#     fig = go.Figure(go.Bar(
#     x=total['importance'],
#     y=total.index,
#     orientation='h' ))

#     fig.update_layout(
#         height=600,
#         width=800,
#         xaxis_title='importance',
#         yaxis_title='',
#         )

#     return st.plotly_chart(fig)


def total_load():
    total = pd.read_csv("DL_Project/Data_csv/total.csv", encoding="utf-8")
    # fig, ax = plt.subplots(figsize=(10, 8))
    # total.plot(kind='barh', ax=ax)
    # st.pyplot(fig)

    st.dataframe(total)
    # fig, ax = plt.subplots(figsize=(10, 8))
    # total.plot(kind='barh', ax=ax)
    # ax.set_xlabel('Importance')
    # ax.set_ylabel('Index')
    # ax.set_yticklabels(total.index)
    # ax.tick_params(axis='y', labelsize=8)
    # plt.tight_layout()
    # st.pyplot(fig)

    # fi = best_model.varimp(use_pandas=True)
    # fi_subset = fi.loc[:, ['variable', 'relative_importance', 'percentage']]
    # fig, ax = plt.subplots(figsize=(16, 12))
    # total_subset.plot(x='variable', y='relative_importance', kind='barh')
    # plt.xlabel('Importance', fontsize=18)
    # plt.ylabel('Variable', fontsize=18)
    # plt.tick_params(axis='y', labelsize=14)
    # plt.tight_layout()
    # plt.show()

    # fig, ax = plt.subplots(figsize=(10, 8))
    # total_subset.plot(kind='barh', ax=ax)
    # ax.set_xlabel('Importance')
    # ax.set_ylabel(total.index)
    # ax.tick_params(axis='y', labelsize=8)
    # plt.tight_layout()
    # plt.show()  

    # fig = go.Figure(go.Bar(x=total['importance'], y=total.index, orientation='h', color=total['importance']))
    # fig.update_layout(
    # height=600,
    # width=800,
    # xaxis_title='importance',
    # yaxis_title='',
    # margin=dict(l=100, r=20, t=30, b=20)
    # )
    # # Streamlit에서 그래프 출력
    # st.plotly_chart(fig)

    # # 막대 그래프 생성
    # fig, ax = plt.pyplot(figsize=(10, 8))
    # total.plot(kind='barh', ax=ax)

    # # 축 레이블 설정
    # ax.set_xlabel('Importance')
    # ax.set_ylabel('Feature')
    # ax.tick_params(axis='y', labelsize=8)

    # # 그래프 레이아웃 설정
    # plt.tight_layout()

    # # Streamlit에서 그래프 출력
    # st.pyplot(fig)


    # fig, ax = plt.subplots()
    # ax.plot(total['importance'])
    # st.pyplot(fig)

    # fig = go.Figure(go.Bar(
    #     x=total['importance'],
    #     y=total.index.astype(str),
    #     orientation='h'))

    # fig.update_layout(
    #     height=600,
    #     width=800,
    #     xaxis_title='importance',
    #     yaxis_title='Index')

    # return st.plotly_chart(fig)




# return st.image("https://i.imgur.com/idnsDBs.gif", width = 1200)
# with st.expander(mecanism_ment()) : mechanism_image()
# def search_result(area, direction) : return st.write(f"### 선택한 결과 입니다. ") 

# def mecanism_ment() : return "# 메커니즘_설명 / 용량이 엄청 클 것 으로 예상 되기에 메모리 최적화. "
# def mechanism_image() : return st.image("https://i.imgur.com/SgRVHOk.jpg", width = 1000)

# def image() : return ["https://i.imgur.com/t4O7ozH.jpg", "https://i.imgur.com/idnsDBs.gif", "https://i.imgur.com/fvRG1Tj.gif"]
# def containers() : return [st.container() for i in range(len(image()))]
    # for i in range(len(image())) :
    #         with containers()[i] : st.image(image()[i], width = 700)



    # image = [
    #     "https://i.imgur.com/t4O7ozH.jpg", 
    #     "https://i.imgur.com/idnsDBs.gif", 
    #     "https://i.imgur.com/fvRG1Tj.gif"
    #     ]

    # for i in range(len(image)) :
    #     with st.expander(f"사진_{i+1}"):
    #         st.image(image[i])


    # containers = [st.container() for i in range(len(image))]
    # for i in range(len(image)) :
    #     with containers[i] : 
    #         st.image(image[i], width = 700)
    # # =====================================================================
    # messages = ['success', 'info', 'warning', 'error']

    # for i in range(3):
    #     for message in messages:
    #         getattr(st, message)(f'{message} 메세지')
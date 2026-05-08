import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 제목
st.title("Title")

# 버튼
if st.button("Recruit Searching"):

    # 데이터 불러오기
    df_saramin = pd.read_csv("data_tmp/data_saramin.csv")
    df_jobkorea = pd.read_csv("data_tmp/data_jobkorea.csv")

    # 데이터 합치기
    df = pd.concat([df_jobkorea, df_saramin], ignore_index=True)

    # 전체 데이터 출력
    st.dataframe(df)

    # 사이트별 개수 계산
    count_df = (
        df["Site"]
        .value_counts()
        .reset_index()
    )

    # 컬럼명 수정
    count_df.columns = ["Site", "Count"]

    # 비율 계산
    count_df["Ratio"] = round(
        count_df["Count"] / count_df["Count"].sum() * 100,
        2
    )

    # 비율 테이블 출력
    st.dataframe(count_df)

    # 파이차트 제목
    st.subheader("Recruitment Ratio")

    # 파이차트
    fig, ax = plt.subplots(figsize=(5, 5))

    ax.pie(
        count_df["Ratio"],
        autopct='%1.1f%%'
    )

    ax.legend(count_df["Site"])

    st.pyplot(fig)

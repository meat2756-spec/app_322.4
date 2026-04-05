import streamlit as st
import math


def calculate_dues(total_amount, num_people, tip_percentage):
    """
    총 금액, 인원 수, 팁 비율을 입력받아 전체 금액과 1인당 부담금을 계산합니다.
    """
    # 1. 팁이 포함된 전체 금액 계산 (소수점 버림)
    total_with_tip = math.floor(total_amount * (1 + tip_percentage / 100))

    # 2. 1인당 부담 금액 계산
    if num_people > 0:
        per_person_raw = total_with_tip / num_people
        # 100단위에서 반올림 (천 단위로 맞춤)
        per_person_rounded = round(per_person_raw, -3)
    else:
        per_person_rounded = 0

    return per_person_rounded, total_with_tip


def main():
    # 인터페이스 제목 설정
    st.title("모임 회비 관리 계산기")
    st.write("금액과 인원수를 입력하여 회비를 계산하세요.")

    # 입력 컴포넌트 구성
    total_input = st.number_input("총 금액(원)", min_value=0, step=1000, value=0)
    people_input = st.number_input("인원 수(명)", min_value=1, step=1, value=1)
    tip_input = st.slider("팁/서비스 비율(%)", min_value=0, max_value=20, value=0, step=1)

    # 계산 결과 가져오기
    per_person, total_tip = calculate_dues(total_input, people_input, tip_input)

    # 출력 컴포넌트 구성
    st.divider()  # 시각적 구분을 위한 선

    col1, col2 = st.columns(2)
    with col1:
        st.metric("1인당 금액(원)", f"{int(per_person):,}")
    with col2:
        st.metric("팁 포함 총 금액(원)", f"{int(total_tip):,}")


if __name__ == "__main__":
    main()
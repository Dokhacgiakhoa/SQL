import streamlit as st
import random
import sqlite3
import pandas as pd
from datetime import datetime
from questions import questions

# --- Database Setup ---
def init_db():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    # Create table with new schema if not exists
    c.execute('''
        CREATE TABLE IF NOT EXISTS quiz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            group_name TEXT,
            score INTEGER,
            total_questions INTEGER,
            percentage REAL,
            date TIMESTAMP
        )
    ''')
    
    # Migration: Attempt to add group_name column if it doesn't exist (for existing DBs)
    try:
        c.execute("ALTER TABLE quiz_results ADD COLUMN group_name TEXT")
    except sqlite3.OperationalError:
        pass # Column likely already exists

    # Migration: Update legacy data (NULL group) to 'Đỗ Khắc Gia Khoa' - 'Vnonymus-02'
    c.execute("UPDATE quiz_results SET group_name = 'Vnonymus-02', username = 'Đỗ Khắc Gia Khoa' WHERE group_name IS NULL OR group_name = ''")
        
    conn.commit()
    return conn

def save_result(username, group_name, score, total):
    conn = init_db()
    c = conn.cursor()
    percentage = (score / total) * 100 if total > 0 else 0
    c.execute('''
        INSERT INTO quiz_results (username, group_name, score, total_questions, percentage, date)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (username, group_name, score, total, percentage, datetime.now()))
    conn.commit()
    conn.close()

def get_leaderboard():
    conn = init_db()
    # Ensure we verify the schema match or just select * safe columns
    try:
        # Removed LIMIT 10 to allow client-side filtering of full dataset
        df = pd.read_sql_query("SELECT username, group_name, score, total_questions, percentage, date FROM quiz_results", conn)
    except:
        # Fallback if query fails
        df = pd.read_sql_query("SELECT username, score, total_questions, percentage, date FROM quiz_results", conn)
    conn.close()
    return df

# --- Page Config & CSS ---
st.set_page_config(
    page_title="SQL Knowledge Hub",
    page_icon="🗄️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    /* Global Styles & Dark Mode */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    
    /* Custom Layout Width - 80% */
    .block-container {
        max-width: 80%;
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 1rem;
        padding-right: 1rem;
        margin: auto;
    }
    
    /* Headers - Neon Effect */
    h1, h2, h3 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #fff !important;
        text-shadow: 0 0 5px #00d2ff, 0 0 10px #00d2ff, 0 0 20px #00d2ff;
    }
    
    p, label, .stMarkdown {
        color: #e0e0e0 !important;
    }
    
    /* Input Fields */
    .stTextInput input {
        background-color: #262730;
        color: #ffffff;
        border: 1px solid #4e4e4e;
    }
    
    /* Question Card */
    .question-container {
        background-color: #1f2937;
        padding: 30px;
        border-radius: 12px;
        border: 1px solid #374151;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 25px;
        transition: transform 0.2s;
    }
    .question-container:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 15px rgba(0, 210, 255, 0.1);
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #00d2ff, #3a7bd5);
        color: white;
        border: none;
        padding: 12px 28px;
        font-weight: bold;
        border-radius: 8px;
        width: 100%;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        opacity: 0.9;
        box-shadow: 0 0 15px rgba(0, 210, 255, 0.5);
    }
    
    /* Success/Error Messages */
    .stSuccess {
        background-color: rgba(6, 95, 70, 0.5);
        color: #34d399;
        border: 1px solid #059669;
    }
    .stError {
        background-color: rgba(127, 29, 29, 0.5);
        color: #f87171;
        border: 1px solid #dc2626;
    }
</style>
""", unsafe_allow_html=True)

# --- Session State ---
if 'page' not in st.session_state:
    st.session_state.page = 'login'  # login, quiz, result
if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = []
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'group_name' not in st.session_state:
    st.session_state.group_name = ""

# --- Helper Functions ---
def start_quiz():
    if not st.session_state.username.strip():
        st.warning("Vui lòng nhập tên của bạn!")
        return
    if not st.session_state.group_name:
        st.warning("Vui lòng chọn nhóm!")
        return
    
    # Filter questions by difficulty
    easy_questions = [q for q in questions if q.get('difficulty') == 'easy']
    medium_questions = [q for q in questions if q.get('difficulty') == 'medium']
    hard_questions = [q for q in questions if q.get('difficulty') == 'hard']
    
    # Sample Logic: 10 Easy, 6 Medium, 4 Hard
    selected_easy = random.sample(easy_questions, min(len(easy_questions), 10))
    selected_medium = random.sample(medium_questions, min(len(medium_questions), 6))
    selected_hard = random.sample(hard_questions, min(len(hard_questions), 4))
    
    # Combine WITHOUT global shuffle to keep order: Easy -> Medium -> Hard
    quiz_pool = selected_easy + selected_medium + selected_hard
    
    # Shuffle options for each selected question
    final_questions = []
    for q in quiz_pool:
        options = q['options'].copy()
        random.shuffle(options)
        final_questions.append({
            'question': q['question'],
            'options': options,
            'answer': q['answer'],
            'explanation': q['explanation'],
            'difficulty': q.get('difficulty', 'easy')
        })
    
    st.session_state.quiz_data = final_questions
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.user_answers = {}
    st.session_state.page = 'quiz'
    st.rerun()

def get_points(difficulty):
    if difficulty == 'easy': return 1
    if difficulty == 'medium': return 2
    if difficulty == 'hard': return 3
    return 1

def submit_answer(selected):
    q_idx = st.session_state.current_index
    current_q = st.session_state.quiz_data[q_idx]
    correct = current_q['answer']
    difficulty = current_q.get('difficulty', 'easy')
    
    st.session_state.user_answers[q_idx] = selected
    if selected == correct:
        st.session_state.score += get_points(difficulty)
    
    if st.session_state.current_index < len(st.session_state.quiz_data) - 1:
        st.session_state.current_index += 1
        st.rerun()
    else:
        # Save result with group name
        save_result(st.session_state.username, st.session_state.group_name, st.session_state.score, 34) 
        st.session_state.page = 'result'
        st.rerun()

# --- Application Flow ---

# 1. Login Screen
if st.session_state.page == 'login':
    st.title("🚀 SQL Challenge")
    st.markdown("### Chào mừng đến với bài kiểm tra SQL tổng hợp")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/919/919836.png", width=150)
    with col2:
        total_q = len(questions)
        st.markdown(f"**Ngân hàng câu hỏi:** {total_q} câu")
        st.markdown("""
        **Cấu trúc bài thi (20 câu - 34 điểm):**
        - Phase 1: 10 câu Dễ (1 điểm/câu)
        - Phase 2: 6 câu Trung bình (2 điểm/câu)
        - Phase 3: 4 câu Khó (3 điểm/câu)
        """)
        st.markdown("---")
        
        # Predefined Users
        user_options = [
            "Lê Trí Phương", "Ngô Tràng Vinh", "Luyện Viết Hào",
            "Đỗ Khắc Gia Khoa", "Nguyễn Xuân Minh Quân", "Lãnh Huy Tiến", "Nguyễn Bình Minh",
            "Nguyễn Đức Khiêm", "Lư Văn Giỏi", "Nguyễn Hoàng Gia", "Trần Hoàng An",
            "Nguyễn Trần Xuân Cường", "Nguyễn Đình Hùng", "Đặng Đình Hùng", "Nguyễn Thanh Phúc",
            "Quang Vinh", "Quang Việt", "Trung Kiên", "Thanh Tùng",
            "Gia Huy", "Minh Tú", "Hoàng Hà",
            "Tuấn Anh", "Quang Minh", "Trọng Tấn"
        ]
        
        # Helper to parse name: Returns (Lastname, Restname)
        def get_name_parts(full_name):
            parts = full_name.strip().split()
            if not parts: return ("", "")
            last_name = parts[-1]
            rest_name = " ".join(parts[:-1])
            return last_name, rest_name

        # Sort by Last Name A-Z
        user_options.sort(key=lambda x: get_name_parts(x)[0])

        def format_user_option(full_name):
            last, rest = get_name_parts(full_name)
            if rest:
                return f"{last} -- {rest}"
            return last

        st.session_state.username = st.selectbox(
            "Chọn tên của bạn:", 
            options=user_options, 
            index=None, 
            format_func=format_user_option,
            placeholder="Tìm tên trong danh sách..."
        )
        group_options = [
            "Vnonymus-01",
            "Vnonymus-02",
            "KING CODE",
            "LUMINOUS MIND",
            "NoName",
            "Nhóm 6",
            "Nhóm 7 (sv không đi học)"
        ]
        
        # UI: "Button with Dropdown" style using Expander + Radio
        # This avoids the 'text input' look of selectbox
        selected_group_label = st.session_state.group_name if st.session_state.group_name else "Chọn nhóm..."
        with st.expander(f"📂 {selected_group_label}"):
            st.session_state.group_name = st.radio(
                "Danh sách nhóm:",
                options=group_options,
                index=None,
                key="group_radio_selection"
            )
        
        if st.button("BẮT ĐẦU NGAY"):
            start_quiz()

    st.markdown("---")
    st.subheader("🏆 Bảng Xếp Hạng")
    
    df = get_leaderboard()
    if not df.empty:
        # --- Aggregation Logic (Max Score & Attempts) ---
        # Calculate attempts count per user
        attempts_count = df['username'].value_counts()
        
        # Pre-process Data for Display
        # Format Date
        if 'date' in df.columns:
            try:
                df['date'] = pd.to_datetime(df['date'])
            except:
                pass

        # Format Score Display
        if 'score' in df.columns and 'total_questions' in df.columns:
            df['score_display'] = df.apply(lambda x: f"{x['score']}/{x['total_questions']}", axis=1)
        else:
            df['score_display'] = df['score']

        # Get unique groups for filter
        unique_groups = df['group_name'].unique().tolist() if 'group_name' in df.columns else []
        unique_groups = [g for g in unique_groups if g]
        
        # Filter Layout
        col_filter1, col_filter2 = st.columns(2)
        with col_filter1:
            selected_group = st.multiselect("Lọc theo Nhóm:", options=unique_groups, placeholder="Chọn nhóm...")
        with col_filter2:
            sort_option = st.selectbox("Sắp xếp theo:", ["Điểm cao nhất", "Mới nhất", "Cũ nhất"], index=0)

        # Apply Group Filter
        filtered_df = df.copy()
        if selected_group and 'group_name' in filtered_df.columns:
            filtered_df = filtered_df[filtered_df['group_name'].isin(selected_group)]

        if filtered_df.empty:
            st.info("Không tìm thấy kết quả phù hợp.")
        else:
            # Group by User to find Best Score and History
            user_data = []
            grouped = filtered_df.groupby('username')
            
            for username, group_df in grouped:
                # Calculate metrics for this user
                real_attempts = len(df[df['username'] == username])

                # Find Best Score (Max Score, then Latest Date)
                best_row = group_df.sort_values(by=['score', 'date'], ascending=[False, False]).iloc[0]
                
                # History (All rows sorted desc by date)
                history_rows = group_df.sort_values(by=['date'], ascending=False)
                
                user_data.append({
                    'username': username,
                    'group_name': best_row.get('group_name', ''),
                    'score': best_row['score'],
                    'date': best_row['date'],
                    'best_row': best_row,
                    'history': history_rows,
                    'attempts': real_attempts
                })

            # Sort the User List
            # 1. Sort by Secondary Criteria (Score/Date)
            if sort_option == "Điểm cao nhất":
                user_data.sort(key=lambda x: (x['score'], x['date']), reverse=True)
            elif sort_option == "Mới nhất":
                user_data.sort(key=lambda x: x['date'], reverse=True)
            else:
                user_data.sort(key=lambda x: x['date'], reverse=False)
            
            # 2. Sort by Primary Criteria (Group) - Stable Sort preserves secondary order
            # Handle empty groups getting pushed to bottom: 'zzzz'
            user_data.sort(key=lambda x: x['group_name'] if x['group_name'] else "zzzz")

        # Custom CSS for "Naked" Buttons (Icon-like)
        st.markdown("""
        <style>
            /* Force transparent background for the history button (7th column) */
            div[data-testid="stHorizontalBlock"] > div:nth-child(7) button {
                background-color: transparent !important;
                background-image: none !important; /* Remove gradient if any */
                border: none !important;
                box-shadow: none !important;
                padding: 0 !important;
                color: inherit !important;
                width: auto !important;
            }
            
            /* Center the button content */
            div[data-testid="stHorizontalBlock"] > div:nth-child(7) div[data-testid="stButton"] {
                display: flex;
                justify-content: center;
            }

            /* Hover effect */
            div[data-testid="stHorizontalBlock"] > div:nth-child(7) button:hover {
                 background-color: transparent !important;
                 color: #00d2ff !important;
                 transform: scale(1.2);
            }
            div[data-testid="stHorizontalBlock"] > div:nth-child(7) button:active {
                background-color: transparent !important;
                color: #00d2ff !important;
            }
            div[data-testid="stHorizontalBlock"] > div:nth-child(7) button:focus {
                background-color: transparent !important;
                color: #00d2ff !important;
                box-shadow: none !important;
                border: none !important;
            }
        </style>
        """, unsafe_allow_html=True)

        if 'selected_user_history' not in st.session_state:
            st.session_state.selected_user_history = None

        # Container with Border for the Table
        with st.container(border=True):
            # --- Render Table Header ---
            # Columns: Group(L), Name(L), MaxScore(R), Pct(R), Attempts(R), Date(R), History(C)
            headers = ["Nhóm/Lớp", "Tên học viên", "Điểm cao nhất", "Tỷ lệ (%)", "Số lần thi", "Thời gian đạt", "Lịch sử"]
            # Adjusted weights for better spacing
            c_weights = [1.5, 2.5, 1.2, 1, 1, 1.5, 1] 
            cols = st.columns(c_weights)
            
            # Helper for Header Styling
            def header_style(text, align="left"):
                return f"<div style='text-align: {align}; font-weight: bold; border-bottom: 1px solid #4e4e4e; padding-bottom: 8px; margin-bottom: 5px;'>{text}</div>"

            # Alignments matching data types
            aligns = ["left", "left", "right", "right", "right", "right", "center"]
            
            for col, header, align in zip(cols, headers, aligns):
                col.markdown(header_style(header, align), unsafe_allow_html=True)
                
            # --- Render Rows ---
            for item in user_data:
                row = item['best_row']
                attempts = item['attempts']
                username = row['username']
                
                date_str = row['date'].strftime('%d/%m/%Y %H:%M') if pd.notnull(row['date']) else ""
                pct = row['percentage']
                pct_str = f"{pct:.2f}"
                
                # Color Coding logic
                if pct >= 80:
                    pct_color = "#28a745" # Green
                elif pct >= 60:
                    pct_color = "#ffc107" # Yellow
                else:
                    pct_color = "#dc3545" # Red
                
                c1, c2, c3, c4, c5, c6, c7 = st.columns(c_weights)
                
                # Helper for Cell Styling
                def cell_style(text, align="left", color=None):
                    style = f"text-align: {align}; padding: 8px 0;"
                    if color:
                        style += f" color: {color}; font-weight: bold;"
                    return f"<div style='{style}'>{text}</div>"

                c1.markdown(cell_style(row.get('group_name', ''), "left"), unsafe_allow_html=True)
                c2.markdown(cell_style(f"**{username}**", "left"), unsafe_allow_html=True)
                c3.markdown(cell_style(str(row['score_display']), "right"), unsafe_allow_html=True)
                c4.markdown(cell_style(pct_str, "right", pct_color), unsafe_allow_html=True)
                c5.markdown(cell_style(str(attempts), "right"), unsafe_allow_html=True)
                c6.markdown(cell_style(date_str, "right"), unsafe_allow_html=True)
                
                if attempts > 1:
                    # Check if this user is currently selected for history
                    is_active = (st.session_state.selected_user_history == username)
                    icon = "📂" if is_active else "📜" 
                    # If active, maybe highlight?
                    
                    if c7.button(icon, key=f"btn_hist_{username}"):
                        if is_active:
                            st.session_state.selected_user_history = None # Toggle off
                        else:
                            st.session_state.selected_user_history = username
                        st.rerun()
                
                st.markdown("<hr style='margin: 0; opacity: 0.1'>", unsafe_allow_html=True)
            
        # --- Render Detached History View ---
        if st.session_state.selected_user_history:
            target_user = st.session_state.selected_user_history
            # Find user data object
            user_obj = next((u for u in user_data if u['username'] == target_user), None)
            
            if user_obj:
                st.markdown("---")
                st.markdown(f"### 📜 Lịch sử làm bài: {target_user}")
                
                history_df = user_obj['history'][['date', 'score_display', 'percentage']].copy()
                history_df['date'] = history_df['date'].dt.strftime('%d/%m/%Y %H:%M:%S')
                history_df.columns = ['Thời gian', 'Điểm số', 'Tỷ lệ (%)']
                
                def color_pct(val):
                    if val >= 80: color = '#28a745'
                    elif val >= 60: color = '#ffc107'
                    else: color = '#dc3545'
                    return f'color: {color}; font-weight: bold;'

                st.dataframe(
                    history_df.style.format("{:.2f}", subset=['Tỷ lệ (%)']).map(color_pct, subset=['Tỷ lệ (%)']),
                    use_container_width=True,
                    hide_index=True
                )
                
                if st.button("Đóng lịch sử"):
                    st.session_state.selected_user_history = None
                    st.rerun()
    else:
        st.info("Chưa có dữ liệu xếp hạng.")

# 2. Quiz Screen
elif st.session_state.page == 'quiz':
    idx = st.session_state.current_index
    total = len(st.session_state.quiz_data)
    q_data = st.session_state.quiz_data[idx]
    
    # Determine current section and progress within section
    current_diff = q_data.get('difficulty', 'easy')
    
    # Calculate section progress
    if idx < 10:
        sec_title = "PHẦN 1: KHỞI ĐỘNG (DỄ)"
        sec_progress = (idx + 1) / 10
        sec_text = f"Câu {idx + 1}/10"
        bg_color = "#28a745"
    elif idx < 16:
        sec_title = "PHẦN 2: TĂNG TỐC (TRUNG BÌNH)"
        sec_progress = (idx - 9) / 6
        sec_text = f"Câu {idx - 9}/6"
        bg_color = "#ffc107"
    else:
        sec_title = "PHẦN 3: VỀ ĐÍCH (KHÓ)"
        sec_progress = (idx - 15) / 4
        sec_text = f"Câu {idx - 15}/4"
        bg_color = "#dc3545"

    st.markdown(f"<h3 style='color: {bg_color} !important;'>{sec_title}</h3>", unsafe_allow_html=True)
    st.progress(sec_progress)
    st.caption(sec_text)
    
    # Question Card
    diff_color = {
        'easy': '#28a745',    # Green
        'medium': '#ffc107',  # Yellow
        'hard': '#dc3545'     # Red
    }
    diff_label = {
        'easy': 'Dễ (1 điểm)',
        'medium': 'Trung bình (2 điểm)',
        'hard': 'Khó (3 điểm)'
    }
    color = diff_color.get(current_diff, '#777')
    label = diff_label.get(current_diff, current_diff)

    st.markdown(f"""
    <div class="question-container">
        <span style="background-color: {color}; padding: 4px 8px; border-radius: 4px; font-size: 0.8em; font-weight: bold; color: white; display: inline-block; margin-bottom: 10px;">{label}</span>
        <h3>{q_data['question']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Options
    selected_option = st.radio(
        "Chọn đáp án:",
        q_data['options'],
        key=f"q_{idx}",
        index=None
    )
    
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("Tiếp theo ➡️"):
            if selected_option:
                submit_answer(selected_option)
            else:
                st.warning("Vui lòng chọn đáp án trước khi tiếp tục!")

# 3. Result Screen
elif st.session_state.page == 'result':
    st.balloons()
    st.title("🎉 Kết Quả Bài Làm")
    
    score = st.session_state.score
    total_score = 34 
    percent = (score / total_score) * 100
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Người chơi", st.session_state.username)
    col2.metric("Nhóm", st.session_state.group_name)
    col3.metric("Điểm số", f"{score}/{total_score}")
    col4.metric("Tỷ lệ đạt", f"{percent:.1f}%")
    
    if percent >= 80:
        st.success("Xuất sắc! Bạn là chuyên gia SQL.")
    elif percent >= 50:
        st.warning("Khá tốt! Hãy tiếp tục phát huy.")
    else:
        st.error("Cần luyện tập thêm nhiều nhé.")
        
    st.markdown("---")
    if st.button("🏠 Quay về trang chủ"):
        st.session_state.page = 'login'
        st.session_state.username = ""
        st.session_state.group_name = ""
        st.session_state.score = 0
        st.session_state.current_index = 0
        st.session_state.user_answers = {}
        st.rerun()
    
    st.markdown("### 🔍 Xem lại đáp án")
    for i, q in enumerate(st.session_state.quiz_data):
        user_ans = st.session_state.user_answers.get(i)
        correct_ans = q['answer']
        diff = q.get('difficulty', 'easy')
        pts = get_points(diff)
        
        with st.expander(f"Câu {i+1} ({diff.upper()} - {pts} điểm): {q['question']}"):
            if user_ans == correct_ans:
                st.success(f"Bạn chọn: {user_ans} (+{pts} điểm)")
            else:
                st.error(f"Bạn chọn: {user_ans} (0 điểm)")
                st.info(f"Đáp án đúng: {correct_ans}")
            st.markdown(f"**Giải thích:** {q['explanation']}")

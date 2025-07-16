import streamlit as st

def format_usernames(usernames, num_lines, usernames_per_line):
    total_usernames = num_lines * usernames_per_line
    selected_usernames = usernames[:total_usernames]

    formatted_lines = []
    for i in range(0, len(selected_usernames), usernames_per_line):
        line = ','.join(selected_usernames[i:i + usernames_per_line])
        formatted_lines.append(line)

    return '\n'.join(formatted_lines)

st.title("📤 Export & Actions: Format Username Lists")

uploaded_file = st.file_uploader("Upload .txt file with 1 username per line", type="txt")

if uploaded_file is not None:
    usernames = uploaded_file.read().decode('utf-8').splitlines()
    usernames = [u.strip() for u in usernames if u.strip()]

    st.write(f"✅ Loaded **{len(usernames)} usernames**")

    num_lines = st.number_input("Number of accounts that gonna perform follow task", min_value=1, max_value=100000, value=5)
    usernames_per_line = st.number_input("Usernames per line", min_value=1, max_value=1000, value=2)

    if st.button("Format and Download"):
        formatted_text = format_usernames(usernames, num_lines, usernames_per_line)
        st.text_area("Preview", formatted_text, height=200)

        st.download_button(
            label="📥 Download Formatted List",
            data=formatted_text,
            file_name="formatted_usernames.txt",
            mime="text/plain"
        )
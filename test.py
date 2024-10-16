import pickle

# Your data
datas = {
    "shabari": {
        "content": ("Shabari is a student who is pursuing his B.Tech in Computer Science and "
                    "Engineering at Knowledge Institute of technology, Kakapalayam, Salem. "
                    "He is a passionate programmer and loves to code. He is also a web developer "
                    "and a competitive programmer. He is also a Machine Learning enthusiast and loves "
                    "to work on projects related to Machine Learning, Artificial Intelligence and "
                    "Ethical Hacking. He is also a content creator and loves to create content on YouTube. "
                    "He is also a mentor and loves to mentor students and help them in their projects "
                    "and assignments. He is also a researcher and loves to do research on various topics. "
                    "He is also a freelancer and loves to work on various projects. He is also a traveler "
                    "and loves to travel to different places. He is also a gamer and loves to play video games. "
                    "He is also a reader and loves to read books. He is also a anime watcher and loves to watch anime. "
                    "He is also a nature lover and loves to spend time in nature. He is also a positive person and "
                    "loves to spread positivity. He is also a motivator and loves to motivate people He is also "
                    "a team player and loves to work in a team. He is also a problem solver and loves to solve problems. "
                    "He is also a risk taker and loves to take risks. He is also a dreamer and loves to dream big. "
                    "He is also a believer and loves to believe in himself. And last he is the one who created me.")
    },
    "jarvis": {
        "content": ("Jarvis is a voice assistant created by Shabari. He is a voice assistant capable of handling wide range of tasks assigned to him. He is a voice assistant created by Shabari. He is a voice assistant capable of handling wide range of tasks assigned to him. He is a voice assistant created by Shabari. He is a voice assistant capable of handling wide range of tasks assigned to him.")
    }
}

# Store the data in a pickle file
with open('jarvis/data/datas.pkl', 'wb') as file:
    pickle.dump(datas, file)

print("Data successfully saved to 'datas.pkl'.")

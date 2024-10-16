from gnewsclient import gnewsclient

def tech_news():
    client = gnewsclient.NewsClient(language='english', 
								location='world', 
								topic='technology', 
								max_results=5)
    return client


def india_tech_news():
    client = gnewsclient.NewsClient(language='english', 
								location='india', 
								topic='technology', 
								max_results=5)
    return client


def nation_news():
	client = gnewsclient.NewsClient(language='english', 
								location='world', 
								topic='nation', 
								max_results=5)
	return client

def entertainment_news():
	client = gnewsclient.NewsClient(language='english', 
								location='world', 
								topic='entertainment', 
								max_results=5)
	return client

def india_entertainment_news():
	client = gnewsclient.NewsClient(language='english', 
								location='india', 
								topic='entertainment', 
								max_results=5)
	return client


def sports_news():
	client = gnewsclient.NewsClient(language='english', 
								location='world', 
								topic='sports', 
								max_results=5)
	return client

def india_sports_news():
	client = gnewsclient.NewsClient(language='english', 
								location='india', 
								topic='sports', 
								max_results=5)
	return client


def world_news():
	client = gnewsclient.NewsClient(language='english', 
								location='world', 
								topic='world', 
								max_results=5)
	return client

def science_news():
	client = gnewsclient.NewsClient(language='english', 
								location='world', 
								topic='science', 
								max_results=5)
	return client

def india_science_news():
	client = gnewsclient.NewsClient(language='english', 
								location='india', 
								topic='science', 
								max_results=5)
	return client

def health_news():
	client = gnewsclient.NewsClient(language='english', 
								location='world', 
								topic='health', 
								max_results=5)
	return client

def india_health_news():
	client = gnewsclient.NewsClient(language='english', 
								location='india', 
								topic='health', 
								max_results=5)
	return client

def business_news():
	client = gnewsclient.NewsClient(language='english', 
								location='world', 
								topic='business', 
								max_results=5)
	return client

def india_business_news():
	client = gnewsclient.NewsClient(language='english', 
								location='india', 
								topic='business', 
								max_results=5)
	return client

def top_news():
	client = gnewsclient.NewsClient(language='english', 
								location='world', 
								topic='top stories', 
								max_results=5)
	return client

def india_top_news():
	client = gnewsclient.NewsClient(language='english', 
								location='india', 
								topic='top stories', 
								max_results=5)
	return client

def manage_news(command):
	if "news about technology in india" in command:
		return True, india_tech_news()
	elif "news about tech" in command:
		return True, tech_news()
	elif "nation news" in command:
		return True, nation_news()
	elif "entertainment news" in command:
		return True, entertainment_news()
	elif "entertainment news in india" in command:
		return True, india_entertainment_news()
	elif "sports news in india" in command:
		return True, india_sports_news()
	elif "sports news" in command:
		return True, sports_news()
	elif "world news" in command:
		return True, world_news()
	elif "science news in india" in command:
		return True, india_science_news()
	elif "science news" in command:
		return True, science_news()
	elif "health news in india" in command:
		return True, india_health_news()
	elif "health news" in command:
		return True, health_news()
	elif "business news in india" in command:
		return True, india_business_news()
	elif "business news" in command:
		return True, business_news()
	elif "top news in india" in command:
		return True, india_top_news()
	elif "top news" in command:
		return True, top_news()	
	else:
		return False, None
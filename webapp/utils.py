from urllib.parse import urlparse, urljoin
from flask import request


# examenation url, where send users (is my url)
def is_safe_url(target):
	ref_url = urlparse(request.host_url)
	test_url = urlparse(urljoin(request.host_url, target))
	return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


# ref_url = urlparse(request.host_url)
# print(ref_url)
# examenation url have 'next', referrer
def get_redirect_target():

	for target in request.values.get('next'), request.referrer:

		referrer = request.referrer
		parsed_url = urlparse(referrer)
	

		if 'None' in str(target) and target is not None:
			# print('1111')
			# target = f"{parsed_url.scheme}://{parsed_url.netloc}/{str(parsed_url.query).replace('next=', '')}"
			if 'next' in str(parsed_url.query): 				
				target = f"{parsed_url.scheme}://{parsed_url.netloc}/{str(parsed_url.query).replace('next=', '')}"
			else:
				target = f"{parsed_url.scheme}://{parsed_url.netloc}/{parsed_url.query}"
		
		elif target is None:
			# print('222')
			target = f"{parsed_url.scheme}://{parsed_url.netloc}/{parsed_url.path}"

		elif 'login' in str(target) and 'news' not in str(target):
			# print('333')
			target = f"{parsed_url.scheme}://{parsed_url.netloc}"
		
		elif 'login' in str(target) and 'news' in str(target):
			# print('444')
			if 'next' in str(parsed_url.query): 				
				target = f"{parsed_url.scheme}://{parsed_url.netloc}/{str(parsed_url.query).replace('next=', '')}"
			else:
				target = f"{parsed_url.scheme}://{parsed_url.netloc}/{parsed_url.query}"
		elif '%' in str(target):
			target = f"{parsed_url.scheme}://{parsed_url.netloc}"


		if not target:
			continue

	return target
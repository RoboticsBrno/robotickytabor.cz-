

install:
	gem install jekyll bundler
	bundle install

serve:
	bundle exec jekyll serve --host 0.0.0.0

serve-live:
	bundle exec jekyll serve --livereload --host 0.0.0.0 --port 4001

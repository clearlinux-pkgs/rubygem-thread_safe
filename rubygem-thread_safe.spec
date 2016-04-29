#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-thread_safe
Version  : 0.3.5
Release  : 13
URL      : https://rubygems.org/downloads/thread_safe-0.3.5.gem
Source0  : https://rubygems.org/downloads/thread_safe-0.3.5.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : ruby
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc

%description
# Threadsafe
[![Gem Version](https://badge.fury.io/rb/thread_safe.svg)](http://badge.fury.io/rb/thread_safe) [![Build Status](https://travis-ci.org/ruby-concurrency/thread_safe.svg?branch=master)](https://travis-ci.org/ruby-concurrency/thread_safe) [![Coverage Status](https://img.shields.io/coveralls/ruby-concurrency/thread_safe/master.svg)](https://coveralls.io/r/ruby-concurrency/thread_safe) [![Code Climate](https://codeclimate.com/github/ruby-concurrency/thread_safe.svg)](https://codeclimate.com/github/ruby-concurrency/thread_safe) [![Dependency Status](https://gemnasium.com/ruby-concurrency/thread_safe.svg)](https://gemnasium.com/ruby-concurrency/thread_safe) [![License](https://img.shields.io/badge/license-apache-green.svg)](http://opensource.org/licenses/MIT) [![Gitter chat](http://img.shields.io/badge/gitter-join%20chat%20%E2%86%92-brightgreen.svg)](https://gitter.im/ruby-concurrency/concurrent-ruby)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n thread_safe-0.3.5
gem spec %{SOURCE0} -l --ruby > rubygem-thread_safe.gemspec

%build
gem build rubygem-thread_safe.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
thread_safe-0.3.5.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/thread_safe-0.3.5.gem
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/README.md
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/examples/bench_cache.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/ext/org/jruby/ext/thread_safe/JRubyCacheBackendLibrary.java
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/ext/org/jruby/ext/thread_safe/jsr166e/ConcurrentHashMap.java
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/ext/org/jruby/ext/thread_safe/jsr166e/ConcurrentHashMapV8.java
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/ext/org/jruby/ext/thread_safe/jsr166e/LongAdder.java
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/ext/org/jruby/ext/thread_safe/jsr166e/Striped64.java
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/ext/org/jruby/ext/thread_safe/jsr166e/nounsafe/ConcurrentHashMapV8.java
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/ext/org/jruby/ext/thread_safe/jsr166e/nounsafe/LongAdder.java
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/ext/org/jruby/ext/thread_safe/jsr166e/nounsafe/Striped64.java
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/ext/org/jruby/ext/thread_safe/jsr166y/ThreadLocalRandom.java
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/ext/thread_safe/JrubyCacheBackendService.java
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/lib/thread_safe.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/lib/thread_safe/atomic_reference_cache_backend.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/lib/thread_safe/cache.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/lib/thread_safe/mri_cache_backend.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/lib/thread_safe/non_concurrent_cache_backend.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/lib/thread_safe/synchronized_cache_backend.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/lib/thread_safe/synchronized_delegator.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/lib/thread_safe/util.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/lib/thread_safe/util/adder.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/lib/thread_safe/util/atomic_reference.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/lib/thread_safe/util/cheap_lockable.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/lib/thread_safe/util/power_of_two_tuple.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/lib/thread_safe/util/striped64.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/lib/thread_safe/util/volatile.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/lib/thread_safe/util/volatile_tuple.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/lib/thread_safe/util/xor_shift_random.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/lib/thread_safe/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/tasks/update_doc.rake
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/test/src/thread_safe/SecurityManager.java
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/test/test_array.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/test/test_cache.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/test/test_cache_loops.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/test/test_hash.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/test/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/test/test_synchronized_delegator.rb
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/thread_safe.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/yard-template/default/fulldoc/html/css/common.css
/usr/lib64/ruby/gems/2.3.0/gems/thread_safe-0.3.5/yard-template/default/layout/html/footer.erb
/usr/lib64/ruby/gems/2.3.0/specifications/thread_safe-0.3.5.gemspec

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-thread_safe
Version  : 0.3.5
Release  : 10
URL      : https://rubygems.org/downloads/thread_safe-0.3.5.gem
Source0  : https://rubygems.org/downloads/thread_safe-0.3.5.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : ruby
BuildRequires : rubygem-ansi
BuildRequires : rubygem-builder
BuildRequires : rubygem-coveralls
BuildRequires : rubygem-docile
BuildRequires : rubygem-domain_name
BuildRequires : rubygem-http-cookie
BuildRequires : rubygem-mime-types
BuildRequires : rubygem-minitest
BuildRequires : rubygem-minitest-reporters
BuildRequires : rubygem-netrc
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rest-client
BuildRequires : rubygem-ruby-progressbar
BuildRequires : rubygem-simplecov
BuildRequires : rubygem-simplecov-html
BuildRequires : rubygem-term-ansicolor
BuildRequires : rubygem-thor
BuildRequires : rubygem-tins
BuildRequires : rubygem-unf
BuildRequires : rubygem-unf_ext

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

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/thread_safe-0.3.5
ruby -v -I.:lib:test test*/test_*.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/thread_safe-0.3.5.gem
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/SynchronizedDelegator/cdesc-SynchronizedDelegator.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/SynchronizedDelegator/method_missing-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/SynchronizedDelegator/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/SynchronizedDelegator/setup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/SynchronizedDelegator/teardown-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Array/cdesc-Array.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/%5b%5d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/%5b%5d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/Node/Util/cdesc-Util.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/Node/cdesc-Node.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/Node/force_aquire_lock-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/Node/key%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/Node/key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/Node/locked%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/Node/locked_hash%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/Node/matches%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/Node/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/Node/pure_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/Node/try_await_lock-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/Node/try_lock_via_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/Node/unlock_via_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/Table/cas_new_node-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/Table/cdesc-Table.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/Table/delete_node_at-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/Table/try_lock_via_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/Table/try_to_cas_in_computed-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/attempt_compute-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/attempt_get_and_set-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/attempt_internal_compute_if_absent-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/attempt_internal_replace-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/cdesc-AtomicReferenceCacheBackend.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/check_for_resize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/clear-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/compute-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/compute_if_absent-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/compute_if_present-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/delete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/delete_pair-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/each_pair-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/empty%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/find_value_in_node_list-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/get_and_set-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/get_or_default-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/initialize_copy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/initialize_table-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/internal_compute-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/internal_replace-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/key%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/key_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/merge_pair-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/replace_if_exists-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/replace_pair-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/table_size_for-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/AtomicReferenceCacheBackend/try_await_lock-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/%5b%5d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/cdesc-Cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/each_key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/each_value-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/empty%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/fetch-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/fetch_or_store-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/get-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/index-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/initialize_copy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/keys-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/marshal_dump-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/marshal_load-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/populate_from-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/put_if_absent-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/raise_fetch_no_key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/validate_options_hash%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/value%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Cache/values-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Hash/cdesc-Hash.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/MriCacheBackend/%5b%5d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/MriCacheBackend/cdesc-MriCacheBackend.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/MriCacheBackend/clear-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/MriCacheBackend/compute-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/MriCacheBackend/compute_if_absent-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/MriCacheBackend/compute_if_present-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/MriCacheBackend/delete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/MriCacheBackend/delete_pair-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/MriCacheBackend/get_and_set-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/MriCacheBackend/merge_pair-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/MriCacheBackend/replace_if_exists-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/MriCacheBackend/replace_pair-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/%5b%5d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/%5b%5d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/_get-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/_set-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/cdesc-NonConcurrentCacheBackend.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/clear-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/compute-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/compute_if_absent-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/compute_if_present-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/delete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/delete_pair-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/dupped_backend-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/each_pair-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/get_and_set-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/get_or_default-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/initialize_copy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/key%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/merge_pair-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/pair%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/replace_if_exists-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/replace_pair-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/store_computed_value-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/NonConcurrentCacheBackend/value%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/SynchronizedCacheBackend/%5b%5d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/SynchronizedCacheBackend/%5b%5d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/SynchronizedCacheBackend/cdesc-SynchronizedCacheBackend.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/SynchronizedCacheBackend/clear-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/SynchronizedCacheBackend/compute-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/SynchronizedCacheBackend/compute_if_absent-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/SynchronizedCacheBackend/compute_if_present-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/SynchronizedCacheBackend/delete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/SynchronizedCacheBackend/delete_pair-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/SynchronizedCacheBackend/dupped_backend-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/SynchronizedCacheBackend/get_and_set-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/SynchronizedCacheBackend/get_or_default-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/SynchronizedCacheBackend/key%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/SynchronizedCacheBackend/merge_pair-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/SynchronizedCacheBackend/replace_if_exists-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/SynchronizedCacheBackend/replace_pair-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/SynchronizedCacheBackend/size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/SynchronizedCacheBackend/value%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Adder/add-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Adder/cdesc-Adder.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Adder/decrement-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Adder/increment-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Adder/reset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Adder/sum-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/CheapLockable/cdesc-CheapLockable.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/CheapLockable/cheap_broadcast-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/CheapLockable/cheap_synchronize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/CheapLockable/cheap_wait-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/PowerOfTwoTuple/cdesc-PowerOfTwoTuple.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/PowerOfTwoTuple/hash_to_index-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/PowerOfTwoTuple/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/PowerOfTwoTuple/next_in_size_table-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/PowerOfTwoTuple/volatile_get_by_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/PowerOfTwoTuple/volatile_set_by_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Striped64/Cell/cas_computed-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Striped64/Cell/cdesc-Cell.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Striped64/cas_base_computed-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Striped64/cdesc-Striped64.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Striped64/expand_table_unless_stale-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Striped64/free%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Striped64/hash_code%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Striped64/hash_code-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Striped64/internal_reset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Striped64/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Striped64/retry_update-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Striped64/try_in_busy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Striped64/try_initialize_cells-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Striped64/try_to_install_new_cell-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Volatile/attr_volatile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/Volatile/cdesc-Volatile.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/VolatileTuple/cas-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/VolatileTuple/cdesc-VolatileTuple.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/VolatileTuple/compare_and_set-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/VolatileTuple/each-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/VolatileTuple/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/VolatileTuple/size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/VolatileTuple/volatile_get-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/VolatileTuple/volatile_set-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/XorShiftRandom/cdesc-XorShiftRandom.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/XorShiftRandom/get-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/XorShiftRandom/xorshift-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/Util/cdesc-Util.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/_mon_initialize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/allocate-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/cdesc-ThreadSafe.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/decrement_size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/increment_size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/lock_and_clean_up_reverse_forwarders-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/rebuild-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/split_bin-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/split_old_bin-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/ThreadSafe/try_in_resize_lock-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/Threadsafe/cdesc-Threadsafe.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/Threadsafe/const_missing-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/thread_safe-0.3.5/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/.travis.yml
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/.yardopts
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/README.md
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/.last_run.json
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/.resultset.json
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/.resultset.json.lock
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/application.css
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/application.js
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/colorbox/border.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/colorbox/controls.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/colorbox/loading.gif
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/colorbox/loading_background.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/favicon_green.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/favicon_red.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/favicon_yellow.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/loading.gif
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/magnify.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/smoothness/images/ui-bg_flat_0_aaaaaa_40x100.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/smoothness/images/ui-bg_flat_75_ffffff_40x100.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/smoothness/images/ui-bg_glass_55_fbf9ee_1x400.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/smoothness/images/ui-bg_glass_65_ffffff_1x400.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/smoothness/images/ui-bg_glass_75_dadada_1x400.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/smoothness/images/ui-bg_glass_75_e6e6e6_1x400.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/smoothness/images/ui-bg_glass_95_fef1ec_1x400.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/smoothness/images/ui-bg_highlight-soft_75_cccccc_1x100.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/smoothness/images/ui-icons_222222_256x240.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/smoothness/images/ui-icons_2e83ff_256x240.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/smoothness/images/ui-icons_454545_256x240.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/smoothness/images/ui-icons_888888_256x240.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/assets/0.10.0/smoothness/images/ui-icons_cd0a0a_256x240.png
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/coverage/index.html
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/examples/bench_cache.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/ext/org/jruby/ext/thread_safe/JRubyCacheBackendLibrary.java
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/ext/org/jruby/ext/thread_safe/jsr166e/ConcurrentHashMap.java
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/ext/org/jruby/ext/thread_safe/jsr166e/ConcurrentHashMapV8.java
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/ext/org/jruby/ext/thread_safe/jsr166e/LongAdder.java
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/ext/org/jruby/ext/thread_safe/jsr166e/Striped64.java
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/ext/org/jruby/ext/thread_safe/jsr166e/nounsafe/ConcurrentHashMapV8.java
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/ext/org/jruby/ext/thread_safe/jsr166e/nounsafe/LongAdder.java
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/ext/org/jruby/ext/thread_safe/jsr166e/nounsafe/Striped64.java
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/ext/org/jruby/ext/thread_safe/jsr166y/ThreadLocalRandom.java
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/ext/thread_safe/JrubyCacheBackendService.java
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/lib/thread_safe.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/lib/thread_safe/atomic_reference_cache_backend.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/lib/thread_safe/cache.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/lib/thread_safe/mri_cache_backend.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/lib/thread_safe/non_concurrent_cache_backend.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/lib/thread_safe/synchronized_cache_backend.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/lib/thread_safe/synchronized_delegator.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/lib/thread_safe/util.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/lib/thread_safe/util/adder.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/lib/thread_safe/util/atomic_reference.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/lib/thread_safe/util/cheap_lockable.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/lib/thread_safe/util/power_of_two_tuple.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/lib/thread_safe/util/striped64.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/lib/thread_safe/util/volatile.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/lib/thread_safe/util/volatile_tuple.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/lib/thread_safe/util/xor_shift_random.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/lib/thread_safe/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/tasks/update_doc.rake
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/test/src/thread_safe/SecurityManager.java
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/test/test_array.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/test/test_cache.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/test/test_cache_loops.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/test/test_hash.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/test/test_helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/test/test_synchronized_delegator.rb
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/thread_safe.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/yard-template/default/fulldoc/html/css/common.css
/usr/lib64/ruby/gems/2.2.0/gems/thread_safe-0.3.5/yard-template/default/layout/html/footer.erb
/usr/lib64/ruby/gems/2.2.0/specifications/thread_safe-0.3.5.gemspec

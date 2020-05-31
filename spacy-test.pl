#!/usr/bin/perl
use Sanitize;
use CGI;
use URI::Escape;

my $q = CGI->new;

my $query = $q->param('query');
#$query = uri_decode($query);

print "Content-Type: text/html\n\n";
print "You searched for: ";
$query = sanitize($query, html => 1);
print $query;
print "<br>";


@list = `/usr/bin/python3 spacy-test.py "$query"`;
print @list;

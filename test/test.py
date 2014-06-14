#-*-coding:utf-8-*-
from autocomplete import Autocomplete
import os
import unittest

class testAutocomplete (unittest.TestCase):
  def setUp (self):
    self.items=[{"uid":'1', "score":9, "term": u"轻轻地你走了"},
                {"uid":'2', "score":10, "term": u"正如你轻轻地来"},
                {"uid":'3', "score":8.5, "term":u"你挥一挥衣袖，不带走一片云彩"},
                ]

    self.a=Autocomplete("scope")
    self.a.del_index()
    for item in self.items:
      self.a.add_item (item)

  def test_search_query2 (self):
    results=self.a.search_query (u'轻轻')
    print "test_search_query2",results
    self.assertEqual(len(results),2)
    self.assertEqual(results[0]['uid'],'2')
    self.assertEqual(results[1]['uid'],'1')

  def test_search_query3 (self):
    results=self.a.search_query (u'你 带走')
    print "test_search_query3",results
    self.assertEqual(len(results),1)

    self.assertEqual(results[0]['uid'],'3')

  def test_search_query4 (self):
    results=self.a.search_query (u'你挥一挥衣袖，不带走一片云彩')
    print "test_search_query4",results
    self.assertEqual(len(results),1)
    self.assertEqual(results[0]['uid'],'3')

  def test_update_item (self):
    item = {"uid":'1', "score":13, "term": u"轻轻地你走了"}
    self.a.update_item (item)
    results=self.a.search_query (u'轻轻')
    self.assertEqual(len(results),2)
    self.assertEqual(results[0]['uid'],'1')
    self.assertEqual(results[1]['uid'],'2')

  def test_del_item (self):
    item = {"uid":'1', "score":9, "term": u"轻轻地你走了"}
    self.a.del_item (item)
    results=self.a.search_query (u'轻轻')
    self.assertEqual(len(results),1)
    self.assertEqual(results[0]['uid'],'2')

if __name__=='__main__':
  unittest.main ()

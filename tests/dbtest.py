import pytest
from ..dbsetup import Vote, Session

def cleanup(sess):
    sess.commit()
    sess.close()

def test_vote_add():
    sess = Session()
    initial_votes = sess.query(Vote).count()
    Vote.add('testimg', 999)
    new_votes = sess.query(Vote).filter(Vote.image == 'testimg').count()
    assert new_votes == initial_votes + 1
    assert (sess.query(Vote).filter(Vote.image == 'testimg')
            .first()).value == 999
    (sess.query(Vote).filter(Vote.image == 'testimg')
     .delete(synchronize_session='fetch'))
    assert (sess.query(Vote).filter(Vote.image == 'testimg')
            .count()) == 0
    cleanup(sess)

def test_vote_mean():
    sess = Session()
    with pytest.raises(ValueError):
        Vote.mean('no_image')
    Vote.add('no_image', 100)
    assert Vote.mean('no_image') == 100
    Vote.add('no_image', 0)
    assert Vote.mean('no_image') == 50

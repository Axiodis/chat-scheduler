from rest_framework import routers

from chats.views.chat import ChatViewSet
from chats.views.conversation import ConversationViewSet

router = routers.SimpleRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'chats', ChatViewSet, basename='chat')
urlpatterns = router.urls

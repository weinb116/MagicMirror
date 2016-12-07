import com.restfb.Connection;
import com.restfb.DefaultFacebookClient;
import com.restfb.FacebookClient;
import com.restfb.types.Post;
import com.restfb.types.User;
import java.util.*;
import java.lang.*;

public class FacebookAPI
{
  public static void public static void main(String[] args) {
    String accessToken = "EAACEdEose0cBAJdavq2O0iKgUJtBNc0DN9gPSDnFjwpAicutyVLGdkL9HSZAvxql5qhTeHPZBkFYow1xAHhahmHM2pVFaoq4GcIFEA8JkBpDunHGQmCkpbtZBQbZAN9VOmhzZATgZBl1jZCZBieFkbmjEbz60g1fz2vLpVyFXHMC8QZDZD"

    FacebookClient client = new DefaultFacebookClient(accessToken);

    Connection<Post> result = client.fetchConnection("me/feed",Post.class);

    for(List<Post> page : result)
    {
      for(Post aPost : page)
      {
        System.out.println(aPost.getMessage());
      }
    }
  }
}

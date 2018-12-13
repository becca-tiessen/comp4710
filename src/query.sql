select
T.Name as 'Post Type',
P.ParentId,
P.Score,
P.ViewCount,
P.Title,
P.Body,
U.Id,
U.DisplayName,
U.Location,
P.AnswerCount,
P.CreationDate

from Posts as P
inner join Users U on P.OwnerUserId = U.Id
inner join PostTypes T on P.PostTypeId = T.Id

where P.CreationDate >= '2018-10-01'
and P.CreationDate < '2018-10-08'
and U.DisplayName not like 'Community'
and T.Name like 'Question'
and P.AnswerCount > 1
and Location is not NULL
and Location NOT LIKE '% %'
and U.DisplayName not like 'user%'

order by U.DisplayName, T.Name, P.Score desc, P.ViewCount desc, P.CreationDate

---
search:
  boost: 10.0
---

# Class: Friend 


_Information about friends in a social network, including aspects of_

_friendships such as years together or nature of friendship_



<div data-search-exclude markdown="1">



URI: [pd:Friend](https://w3id.org/lmodel/dpv/pd/Friend)





```mermaid
 classDiagram
    class Friend
    click Friend href "../Friend/"
      SocialNetwork <|-- Friend
        click SocialNetwork href "../SocialNetwork/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [SocialNetwork](SocialNetwork.md)
        * **Friend**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Friend](https://w3id.org/lmodel/dpv/pd/Friend) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Friend




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Friend |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Friend |
| native | pd:Friend |
| exact | dpv_pd:Friend, dpv_pd_owl:Friend |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Friend
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Friend
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about friends in a social network, including aspects of

  friendships such as years together or nature of friendship'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Friend
exact_mappings:
- dpv_pd:Friend
- dpv_pd_owl:Friend
is_a: SocialNetwork
class_uri: pd:Friend

```
</details>

### Induced

<details>
```yaml
name: Friend
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Friend
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about friends in a social network, including aspects of

  friendships such as years together or nature of friendship'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Friend
exact_mappings:
- dpv_pd:Friend
- dpv_pd_owl:Friend
is_a: SocialNetwork
class_uri: pd:Friend

```
</details></div>
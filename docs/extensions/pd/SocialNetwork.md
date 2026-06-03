---
search:
  boost: 10.0
---

# Class: SocialNetwork 


_Information about friends or connections expressed as a social network_



<div data-search-exclude markdown="1">



URI: [pd:SocialNetwork](https://w3id.org/lmodel/dpv/pd/SocialNetwork)





```mermaid
 classDiagram
    class SocialNetwork
    click SocialNetwork href "../SocialNetwork/"
      Social <|-- SocialNetwork
        click Social href "../Social/"
      

      SocialNetwork <|-- Acquaintance
        click Acquaintance href "../Acquaintance/"
      SocialNetwork <|-- Association
        click Association href "../Association/"
      SocialNetwork <|-- Connection
        click Connection href "../Connection/"
      SocialNetwork <|-- Friend
        click Friend href "../Friend/"
      SocialNetwork <|-- GroupMembership
        click GroupMembership href "../GroupMembership/"
      

      
```





## Inheritance
* [Social](Social.md)
    * **SocialNetwork**
        * [Acquaintance](Acquaintance.md)
        * [Association](Association.md)
        * [Connection](Connection.md)
        * [Friend](Friend.md)
        * [GroupMembership](GroupMembership.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:SocialNetwork](https://w3id.org/lmodel/dpv/pd/SocialNetwork) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Social Network




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#SocialNetwork |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:SocialNetwork |
| native | pd:SocialNetwork |
| exact | dpv_pd:SocialNetwork, dpv_pd_owl:SocialNetwork |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SocialNetwork
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#SocialNetwork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about friends or connections expressed as a social network
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Social Network
exact_mappings:
- dpv_pd:SocialNetwork
- dpv_pd_owl:SocialNetwork
is_a: Social
class_uri: pd:SocialNetwork

```
</details>

### Induced

<details>
```yaml
name: SocialNetwork
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#SocialNetwork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about friends or connections expressed as a social network
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Social Network
exact_mappings:
- dpv_pd:SocialNetwork
- dpv_pd_owl:SocialNetwork
is_a: Social
class_uri: pd:SocialNetwork

```
</details></div>
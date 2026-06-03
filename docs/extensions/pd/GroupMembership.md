---
search:
  boost: 10.0
---

# Class: GroupMembership 


_Information about groups and memberships included or associated with a_

_social network_



<div data-search-exclude markdown="1">



URI: [pd:GroupMembership](https://w3id.org/lmodel/dpv/pd/GroupMembership)





```mermaid
 classDiagram
    class GroupMembership
    click GroupMembership href "../GroupMembership/"
      SocialNetwork <|-- GroupMembership
        click SocialNetwork href "../SocialNetwork/"
      

      GroupMembership <|-- TradeUnionMembership
        click TradeUnionMembership href "../TradeUnionMembership/"
      

      
```





## Inheritance
* [Social](Social.md)
    * [SocialNetwork](SocialNetwork.md)
        * **GroupMembership**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:GroupMembership](https://w3id.org/lmodel/dpv/pd/GroupMembership) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Group Membership




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#GroupMembership |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:GroupMembership |
| native | pd:GroupMembership |
| exact | dpv_pd:GroupMembership, dpv_pd_owl:GroupMembership |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GroupMembership
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#GroupMembership
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about groups and memberships included or associated with
  a

  social network'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Group Membership
exact_mappings:
- dpv_pd:GroupMembership
- dpv_pd_owl:GroupMembership
is_a: SocialNetwork
class_uri: pd:GroupMembership

```
</details>

### Induced

<details>
```yaml
name: GroupMembership
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#GroupMembership
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about groups and memberships included or associated with
  a

  social network'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Group Membership
exact_mappings:
- dpv_pd:GroupMembership
- dpv_pd_owl:GroupMembership
is_a: SocialNetwork
class_uri: pd:GroupMembership

```
</details></div>
---
search:
  boost: 10.0
---

# Class: Association 


_Information about associations in a social network with other_

_individuals, groups, or entities e.g. friend of a friend_



<div data-search-exclude markdown="1">



URI: [pd:Association](https://w3id.org/lmodel/dpv/pd/Association)





```mermaid
 classDiagram
    class Association
    click Association href "../Association/"
      SocialNetwork <|-- Association
        click SocialNetwork href "../SocialNetwork/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [SocialNetwork](SocialNetwork.md)
        * **Association**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Association](https://w3id.org/lmodel/dpv/pd/Association) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Association




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Association |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Association |
| native | pd:Association |
| exact | dpv_pd:Association, dpv_pd_owl:Association |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Association
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Association
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about associations in a social network with other

  individuals, groups, or entities e.g. friend of a friend'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Association
exact_mappings:
- dpv_pd:Association
- dpv_pd_owl:Association
is_a: SocialNetwork
class_uri: pd:Association

```
</details>

### Induced

<details>
```yaml
name: Association
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Association
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about associations in a social network with other

  individuals, groups, or entities e.g. friend of a friend'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Association
exact_mappings:
- dpv_pd:Association
- dpv_pd_owl:Association
is_a: SocialNetwork
class_uri: pd:Association

```
</details></div>
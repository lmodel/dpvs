---
search:
  boost: 10.0
---

# Class: Acquaintance 


_Information about acquaintances in a social network_



<div data-search-exclude markdown="1">



URI: [pd:Acquaintance](https://w3id.org/lmodel/dpv/pd/Acquaintance)





```mermaid
 classDiagram
    class Acquaintance
    click Acquaintance href "../Acquaintance/"
      SocialNetwork <|-- Acquaintance
        click SocialNetwork href "../SocialNetwork/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [SocialNetwork](SocialNetwork.md)
        * **Acquaintance**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Acquaintance](https://w3id.org/lmodel/dpv/pd/Acquaintance) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Acquaintance




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Acquaintance |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Acquaintance |
| native | pd:Acquaintance |
| exact | dpv_pd:Acquaintance, dpv_pd_owl:Acquaintance |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Acquaintance
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Acquaintance
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about acquaintances in a social network
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Acquaintance
exact_mappings:
- dpv_pd:Acquaintance
- dpv_pd_owl:Acquaintance
is_a: SocialNetwork
class_uri: pd:Acquaintance

```
</details>

### Induced

<details>
```yaml
name: Acquaintance
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Acquaintance
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about acquaintances in a social network
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Acquaintance
exact_mappings:
- dpv_pd:Acquaintance
- dpv_pd_owl:Acquaintance
is_a: SocialNetwork
class_uri: pd:Acquaintance

```
</details></div>
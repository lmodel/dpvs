---
search:
  boost: 10.0
---

# Class: Relationship 


_Information about relationships and relationship history_



<div data-search-exclude markdown="1">



URI: [pd:Relationship](https://w3id.org/lmodel/dpv/pd/Relationship)





```mermaid
 classDiagram
    class Relationship
    click Relationship href "../Relationship/"
      Family <|-- Relationship
        click Family href "../Family/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Family](Family.md)
        * **Relationship**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Relationship](https://w3id.org/lmodel/dpv/pd/Relationship) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Relationship




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Relationship |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Relationship |
| native | pd:Relationship |
| exact | dpv_pd:Relationship, dpv_pd_owl:Relationship |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Relationship
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Relationship
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about relationships and relationship history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Relationship
exact_mappings:
- dpv_pd:Relationship
- dpv_pd_owl:Relationship
is_a: Family
class_uri: pd:Relationship

```
</details>

### Induced

<details>
```yaml
name: Relationship
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Relationship
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about relationships and relationship history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Relationship
exact_mappings:
- dpv_pd:Relationship
- dpv_pd_owl:Relationship
is_a: Family
class_uri: pd:Relationship

```
</details></div>
---
search:
  boost: 10.0
---

# Class: Sibling 


_Information about sibling(s)_



<div data-search-exclude markdown="1">



URI: [pd:Sibling](https://w3id.org/lmodel/dpv/pd/Sibling)





```mermaid
 classDiagram
    class Sibling
    click Sibling href "../Sibling/"
      FamilyStructure <|-- Sibling
        click FamilyStructure href "../FamilyStructure/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Family](Family.md)
        * [FamilyStructure](FamilyStructure.md)
            * **Sibling**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Sibling](https://w3id.org/lmodel/dpv/pd/Sibling) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Sibling




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Sibling |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Sibling |
| native | pd:Sibling |
| exact | dpv_pd:Sibling, dpv_pd_owl:Sibling |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Sibling
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Sibling
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about sibling(s)
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Sibling
exact_mappings:
- dpv_pd:Sibling
- dpv_pd_owl:Sibling
is_a: FamilyStructure
class_uri: pd:Sibling

```
</details>

### Induced

<details>
```yaml
name: Sibling
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Sibling
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about sibling(s)
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Sibling
exact_mappings:
- dpv_pd:Sibling
- dpv_pd_owl:Sibling
is_a: FamilyStructure
class_uri: pd:Sibling

```
</details></div>
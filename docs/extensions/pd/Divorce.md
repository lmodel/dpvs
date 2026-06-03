---
search:
  boost: 10.0
---

# Class: Divorce 


_Information about divorce(s)_



<div data-search-exclude markdown="1">



URI: [pd:Divorce](https://w3id.org/lmodel/dpv/pd/Divorce)





```mermaid
 classDiagram
    class Divorce
    click Divorce href "../Divorce/"
      FamilyStructure <|-- Divorce
        click FamilyStructure href "../FamilyStructure/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Family](Family.md)
        * [FamilyStructure](FamilyStructure.md)
            * **Divorce**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Divorce](https://w3id.org/lmodel/dpv/pd/Divorce) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Divorce




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Divorce |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Divorce |
| native | pd:Divorce |
| exact | dpv_pd:Divorce, dpv_pd_owl:Divorce |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Divorce
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Divorce
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about divorce(s)
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Divorce
exact_mappings:
- dpv_pd:Divorce
- dpv_pd_owl:Divorce
is_a: FamilyStructure
class_uri: pd:Divorce

```
</details>

### Induced

<details>
```yaml
name: Divorce
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Divorce
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about divorce(s)
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Divorce
exact_mappings:
- dpv_pd:Divorce
- dpv_pd_owl:Divorce
is_a: FamilyStructure
class_uri: pd:Divorce

```
</details></div>
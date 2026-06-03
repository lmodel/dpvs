---
search:
  boost: 10.0
---

# Class: FamilyStructure 


_Information about family and familial structure_



<div data-search-exclude markdown="1">



URI: [pd:FamilyStructure](https://w3id.org/lmodel/dpv/pd/FamilyStructure)





```mermaid
 classDiagram
    class FamilyStructure
    click FamilyStructure href "../FamilyStructure/"
      Family <|-- FamilyStructure
        click Family href "../Family/"
      

      FamilyStructure <|-- Divorce
        click Divorce href "../Divorce/"
      FamilyStructure <|-- Marriage
        click Marriage href "../Marriage/"
      FamilyStructure <|-- Offspring
        click Offspring href "../Offspring/"
      FamilyStructure <|-- Parent
        click Parent href "../Parent/"
      FamilyStructure <|-- Sibling
        click Sibling href "../Sibling/"
      

      
```





## Inheritance
* [Social](Social.md)
    * [Family](Family.md)
        * **FamilyStructure**
            * [Divorce](Divorce.md)
            * [Marriage](Marriage.md)
            * [Offspring](Offspring.md)
            * [Parent](Parent.md)
            * [Sibling](Sibling.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:FamilyStructure](https://w3id.org/lmodel/dpv/pd/FamilyStructure) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Family Structure




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#FamilyStructure |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:FamilyStructure |
| native | pd:FamilyStructure |
| exact | dpv_pd:FamilyStructure, dpv_pd_owl:FamilyStructure |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FamilyStructure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FamilyStructure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about family and familial structure
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Family Structure
exact_mappings:
- dpv_pd:FamilyStructure
- dpv_pd_owl:FamilyStructure
is_a: Family
class_uri: pd:FamilyStructure

```
</details>

### Induced

<details>
```yaml
name: FamilyStructure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FamilyStructure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about family and familial structure
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Family Structure
exact_mappings:
- dpv_pd:FamilyStructure
- dpv_pd_owl:FamilyStructure
is_a: Family
class_uri: pd:FamilyStructure

```
</details></div>
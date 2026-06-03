---
search:
  boost: 10.0
---

# Class: Family 


_Information about family and relationships_



<div data-search-exclude markdown="1">



URI: [pd:Family](https://w3id.org/lmodel/dpv/pd/Family)





```mermaid
 classDiagram
    class Family
    click Family href "../Family/"
      Social <|-- Family
        click Social href "../Social/"
      

      Family <|-- FamilyStructure
        click FamilyStructure href "../FamilyStructure/"
      Family <|-- Relationship
        click Relationship href "../Relationship/"
      

      
```





## Inheritance
* [Social](Social.md)
    * **Family**
        * [FamilyStructure](FamilyStructure.md)
        * [Relationship](Relationship.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Family](https://w3id.org/lmodel/dpv/pd/Family) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Family




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Family |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Family |
| native | pd:Family |
| exact | dpv_pd:Family, dpv_pd_owl:Family |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Family
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Family
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about family and relationships
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Family
exact_mappings:
- dpv_pd:Family
- dpv_pd_owl:Family
is_a: Social
class_uri: pd:Family

```
</details>

### Induced

<details>
```yaml
name: Family
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Family
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about family and relationships
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Family
exact_mappings:
- dpv_pd:Family
- dpv_pd_owl:Family
is_a: Social
class_uri: pd:Family

```
</details></div>
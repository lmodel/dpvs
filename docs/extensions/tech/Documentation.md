---
search:
  boost: 10.0
---

# Class: Documentation 


_Information describing use, functionality, design, or other technical_

_aspects of the Technology_



<div data-search-exclude markdown="1">



URI: [tech:Documentation](https://w3id.org/lmodel/dpv/tech/Documentation)





```mermaid
 classDiagram
    class Documentation
    click Documentation href "../Documentation/"
      Documentation <|-- DevelopmentPlan
        click DevelopmentPlan href "../DevelopmentPlan/"
      Documentation <|-- Guide
        click Guide href "../Guide/"
      Documentation <|-- Instructions
        click Instructions href "../Instructions/"
      Documentation <|-- Manual
        click Manual href "../Manual/"
      Documentation <|-- Plan
        click Plan href "../Plan/"
      Documentation <|-- Specification
        click Specification href "../Specification/"
      Documentation <|-- TestingPlan
        click TestingPlan href "../TestingPlan/"
      
      
```





## Inheritance
* **Documentation**
    * [Guide](Guide.md)
    * [Instructions](Instructions.md)
    * [Manual](Manual.md)
    * [Plan](Plan.md)
    * [Specification](Specification.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Documentation](https://w3id.org/lmodel/dpv/tech/Documentation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Documentation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Documentation |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Documentation |
| native | tech:Documentation |
| exact | dpv_tech:Documentation, dpv_tech_owl:Documentation |
| close | iso22989:Documentation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Documentation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Documentation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Information describing use, functionality, design, or other technical

  aspects of the Technology'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Documentation
exact_mappings:
- dpv_tech:Documentation
- dpv_tech_owl:Documentation
close_mappings:
- iso22989:Documentation
class_uri: tech:Documentation

```
</details>

### Induced

<details>
```yaml
name: Documentation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Documentation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Information describing use, functionality, design, or other technical

  aspects of the Technology'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Documentation
exact_mappings:
- dpv_tech:Documentation
- dpv_tech_owl:Documentation
close_mappings:
- iso22989:Documentation
class_uri: tech:Documentation

```
</details></div>
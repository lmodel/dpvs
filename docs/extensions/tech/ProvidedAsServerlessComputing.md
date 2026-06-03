---
search:
  boost: 10.0
---

# Class: ProvidedAsServerlessComputing 


_Technology provided as a cloud service consisting of fully managed_

_servers for executing functions_



<div data-search-exclude markdown="1">



URI: [tech:ProvidedAsServerlessComputing](https://w3id.org/lmodel/dpv/tech/ProvidedAsServerlessComputing)





```mermaid
 classDiagram
    class ProvidedAsServerlessComputing
    click ProvidedAsServerlessComputing href "../ProvidedAsServerlessComputing/"
      ProvisionMethod <|-- ProvidedAsServerlessComputing
        click ProvisionMethod href "../ProvisionMethod/"
      ProvidedAsCloudService <|-- ProvidedAsServerlessComputing
        click ProvidedAsCloudService href "../ProvidedAsCloudService/"
      
      
```





## Inheritance
* [ProvisionMethod](ProvisionMethod.md)
    * [ProvidedAsService](ProvidedAsService.md)
        * [ProvidedAsCloudService](ProvidedAsCloudService.md) [ [ProvisionMethod](ProvisionMethod.md)]
            * **ProvidedAsServerlessComputing** [ [ProvisionMethod](ProvisionMethod.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ProvidedAsServerlessComputing](https://w3id.org/lmodel/dpv/tech/ProvidedAsServerlessComputing) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provided as Serverless ComputingProvision




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ProvidedAsServerlessComputing |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ProvidedAsServerlessComputing |
| native | tech:ProvidedAsServerlessComputing |
| exact | dpv_tech:ProvidedAsServerlessComputing, dpv_tech_owl:ProvidedAsServerlessComputing |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvidedAsServerlessComputing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsServerlessComputing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Technology provided as a cloud service consisting of fully managed

  servers for executing functions'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Serverless ComputingProvision
exact_mappings:
- dpv_tech:ProvidedAsServerlessComputing
- dpv_tech_owl:ProvidedAsServerlessComputing
is_a: ProvidedAsCloudService
mixins:
- ProvisionMethod
class_uri: tech:ProvidedAsServerlessComputing

```
</details>

### Induced

<details>
```yaml
name: ProvidedAsServerlessComputing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsServerlessComputing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Technology provided as a cloud service consisting of fully managed

  servers for executing functions'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Serverless ComputingProvision
exact_mappings:
- dpv_tech:ProvidedAsServerlessComputing
- dpv_tech_owl:ProvidedAsServerlessComputing
is_a: ProvidedAsCloudService
mixins:
- ProvisionMethod
class_uri: tech:ProvidedAsServerlessComputing

```
</details></div>